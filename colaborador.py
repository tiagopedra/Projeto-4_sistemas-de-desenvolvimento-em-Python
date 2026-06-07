from typing import List, Optional


class Colaborador:

    def __init__(
        self,
        nome: str,
        cargo: str,
        salario: float,
        matricula: int,
        dependentes: int = 0,
        beneficios: Optional[List[str]] = None
    ):

        # -------------------------
        # VALIDAÇÕES
        # -------------------------

        if salario < 0:
            raise ValueError("Salário não pode ser negativo")

        if dependentes < 0:
            raise ValueError("Número de dependentes inválido")

        if not nome.strip():
            raise ValueError("Nome não pode ser vazio")

        if not cargo.strip():
            raise ValueError("Cargo não pode ser vazio")

        # -------------------------
        # ATRIBUTOS
        # -------------------------

        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.matricula = matricula
        self.dependentes = dependentes
        self.beneficios = list(beneficios) if beneficios else []

    # -------------------------
    # ATUALIZAR DADOS
    # -------------------------

    def atualizar_dados(
        self,
        nome=None,
        cargo=None,
        salario=None,
        dependentes=None,
        beneficios=None
    ):

        if nome is not None:

            if not nome.strip():
                raise ValueError("Nome não pode ser vazio")

            self.nome = nome

        if cargo is not None:

            if not cargo.strip():
                raise ValueError("Cargo não pode ser vazio")

            self.cargo = cargo

        if salario is not None:

            if salario < 0:
                raise ValueError("Salário inválido")

            self.salario = salario

        if dependentes is not None:

            if dependentes < 0:
                raise ValueError("Número de dependentes inválido")

            self.dependentes = dependentes

        if beneficios is not None:
            self.beneficios = list(beneficios)

    # -------------------------
    # BENEFÍCIOS
    # -------------------------

    def adicionar_beneficio(self, beneficio):

        if beneficio not in self.beneficios:
            self.beneficios.append(beneficio)

    def remover_beneficio(self, beneficio):

        if beneficio in self.beneficios:
            self.beneficios.remove(beneficio)

    # -------------------------
    # CONVERSÃO
    # -------------------------

    def to_dict(self):

        return {
            "matricula": self.matricula,
            "nome": self.nome,
            "cargo": self.cargo,
            "salario": self.salario,
            "dependentes": self.dependentes,
            "beneficios": self.beneficios
        }

    # -------------------------
    # EXIBIÇÃO
    # -------------------------

    def __str__(self):

        beneficios_str = (
            ", ".join(self.beneficios)
            if self.beneficios
            else "Nenhum"
        )

        return (
            f"Matrícula: {self.matricula} | "
            f"Nome: {self.nome} | "
            f"Cargo: {self.cargo} | "
            f"Salário: R$ {self.salario:.2f} | "
            f"Número de Dependentes: {self.dependentes} | "
            f"Benefícios: {beneficios_str}"
        )