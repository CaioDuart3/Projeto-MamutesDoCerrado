from django.test import TestCase
from stock.models import Tool

class ToolModelTest(TestCase):
    
    def setUp(self):
        """Configura o ambiente de teste criando uma instância do modelo Tool"""
        self.tool = Tool.objects.create(
            name='Hammer',
            brand='XYZ',
            quantity=10,
            observation='Used for construction.',
            location='Toolbox 1',
            being_used=False
        )

    def test_tool_creation(self):
        """Testa a criação de uma instância do modelo Tool"""
        tool = self.tool
        self.assertEqual(tool.name, 'Hammer')  # Verifica se o nome foi atribuído corretamente
        self.assertEqual(tool.brand, 'XYZ')  
        self.assertEqual(tool.quantity, 10) 
        self.assertEqual(tool.observation, 'Used for construction.') 
        self.assertEqual(tool.location, 'Toolbox 1')  
        self.assertFalse(tool.being_used)  

    def test_str_method(self):
        """Testa o método __str__ do modelo Tool"""
        tool = self.tool
        self.assertEqual(str(tool), 'Hammer')  # Verifica se o método __str__ retorna o nome da ferramenta

    def test_tool_default_values(self):
        """Testa se os valores padrões estão funcionando corretamente"""
        # Criação de uma ferramenta sem passar valores para alguns campos
        tool = Tool.objects.create(
            name='Screwdriver',
            brand='ABC',
            quantity=5,
            location='Toolbox 2'
        )
        
        self.assertEqual(tool.observation, None) 
        self.assertFalse(tool.being_used) 