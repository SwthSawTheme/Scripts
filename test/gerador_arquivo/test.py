import os
import unittest
from main import logs, file_generator  # Importe as funções do seu arquivo main.py

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # Configurações iniciais antes de cada teste
        self.test_dir = "test_temp"
        os.makedirs(self.test_dir, exist_ok=True)
        self.log_file = os.path.join(self.test_dir, "logs.txt")
        self.settings_file = os.path.join(self.test_dir, "settings.txt")

    def tearDown(self):
        # Limpeza após cada teste
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
        if os.path.exists(self.settings_file):
            os.remove(self.settings_file)
        if os.path.exists(self.test_dir) and not os.listdir(self.test_dir):
            os.rmdir(self.test_dir)

    def test_logs_success(self):
        # Testa a geração de log com sucesso
        result = logs("Test error message")
        self.assertEqual(result, "Log gerado com sucesso!")
        with open(self.log_file, "r") as file:
            content = file.read()
            self.assertIn("Test error message", content)

    def test_logs_oserror(self):
        # Testa o comportamento com erro de permissão (simulado)
        # Primeiro, tentamos criar um arquivo sem permissão de escrita
        with open(self.log_file, "w") as file:
            file.write("locked")
        os.chmod(self.log_file, 0o444)  # Define como somente leitura
        result = logs("Another error message")
        self.assertEqual(result, "Não foi possível gerar ou atualizar o arquivo de log!")
        os.chmod(self.log_file, 0o666)  # Restaura permissões

    def test_file_generator_success(self):
        # Testa a geração de arquivo settings.txt com sucesso
        result = file_generator("Test data")
        self.assertEqual(result, "Arquivo settings.txt atualizado com sucesso!")
        with open(self.settings_file, "r") as file:
            content = file.read()
            self.assertIn("Test data", content)

    def test_file_generator_oserror(self):
        # Testa o comportamento com erro de I/O
        # Cria um diretório temporário e tenta escrever fora dele
        temp_path = os.path.join(self.test_dir, "subfolder")
        os.makedirs(temp_path, exist_ok=True)
        invalid_path = os.path.join(temp_path, "settings.txt")
        os.chmod(temp_path, 0o555)  # Define como somente leitura
        result = file_generator("Invalid data")
        self.assertEqual(result, "Erro ao acessar o arquivo! Log gerado.")
        os.chmod(temp_path, 0o755)  # Restaura permissões

    def test_main_execution(self):
        # Testa a execução do bloco if __name__ == "__main__"
        # Simula entrada do usuário
        import io
        import sys
        sys.stdin = io.StringIO("Test input\n")
        # Captura a saída
        from contextlib import redirect_stdout
        import StringIO
        f = StringIO.StringIO()
        with redirect_stdout(f):
            import main
        output = f.getvalue().strip()
        self.assertIn("Arquivo settings.txt atualizado com sucesso!", output)
        sys.stdin = sys.__stdin__  # Restaura entrada padrão

if __name__ == "__main__":
    unittest.main()