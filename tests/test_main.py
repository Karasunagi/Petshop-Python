from app.main import build_menu, handle_choice
from app.services.pet_service import PetShopService


def test_build_menu_contains_options():
    menu = build_menu()

    assert "1. Cadastrar cliente" in menu
    assert "2. Listar clientes" in menu
    assert "11. Cadastrar produto" in menu
    assert "12. Listar produtos" in menu
    assert "0. Sair" in menu


def test_handle_choice_registers_client(tmp_path):
    clientes_path = tmp_path / "test_clientes_menu.json"
    animais_path = tmp_path / "test_animais_menu.json"
    service = PetShopService(
        clients_path=str(clientes_path),
        animals_path=str(animais_path),
    )

    result = handle_choice(service, "1", ["Maria", "11999999999", "maria@email.com"])

    assert result["nome"] == "Maria"
    assert result["email"] == "maria@email.com"


def test_handle_choice_registers_product(tmp_path):
    service = PetShopService(
        clients_path=str(tmp_path / "test_clientes.json"),
        animals_path=str(tmp_path / "test_animais.json"),
        products_path=str(tmp_path / "test_produtos.json"),
    )

    result = handle_choice(service, "11", ["Ração", "Alimento", "Marca A", "25.5", "10", "Fornecedor"])

    assert result["nome"] == "Ração"
    assert result["preco"] == 25.5
    assert result["quantidade"] == 10
