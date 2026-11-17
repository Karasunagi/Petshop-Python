from app.services.pet_service import PetShopService


def test_cadastrar_e_listar_clientes(tmp_path):
    clientes_path = tmp_path / "test_clientes.json"
    animais_path = tmp_path / "test_animais.json"
    service = PetShopService(clients_path=str(clientes_path), animals_path=str(animais_path))

    cliente = service.cadastrar_cliente("Maria", "11999999999", "maria@email.com")

    assert cliente["nome"] == "Maria"
    assert cliente["id"] == 1
    assert len(service.listar_clientes()) == 1


def test_cadastrar_e_listar_animais(tmp_path):
    clientes_path = tmp_path / "test_clientes.json"
    animais_path = tmp_path / "test_animais.json"
    service = PetShopService(clients_path=str(clientes_path), animals_path=str(animais_path))

    service.cadastrar_cliente("João", "11888888888", "joao@email.com")
    animal = service.cadastrar_animal("Rex", "Cachorro", "Vira-lata", 3, 1)

    assert animal["nome"] == "Rex"
    assert animal["dono_id"] == 1
    assert len(service.listar_animais()) == 1


def test_cadastrar_atualizar_buscar_e_excluir_produto(tmp_path):
    service = PetShopService(
        clients_path=str(tmp_path / "test_clientes.json"),
        animals_path=str(tmp_path / "test_animais.json"),
        products_path=str(tmp_path / "test_produtos.json"),
    )

    produto = service.cadastrar_produto(" Ração ", "Alimento", "Marca A", 25.5, 10, "Fornecedor")

    assert produto["nome"] == "Ração"
    assert produto["id"] == 1
    assert service.buscar_produto(1).nome == "Ração"
    assert len(service.listar_produtos()) == 1

    atualizado = service.atualizar_produto(1, "Ração Premium", "Alimento", "Marca A", 30, 8, "Fornecedor")

    assert atualizado["nome"] == "Ração Premium"
    assert service.buscar_produto(1).quantidade == 8
    assert service.excluir_produto(1) is True
    assert service.listar_produtos() == []
