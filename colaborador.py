class Colaborador:
    def __init__(self, nome, cargo, salario, matricula, dependentes=0, beneficios=None):
        # Garantindo valores válidos
        self.nome = nome
        self.cargo = cargo
        self.salario = max(0, salario)  # nunca negativo
        self.matricula = matricula
        self.dependentes = max(0, dependentes)  # nunca negativo
        self.beneficios = beneficios if beneficios else []

    def atualizar_dados(self, nome=None, cargo=None, salario=None, dependentes=None, beneficios=None):
        if nome:
            self.nome = nome
        if cargo:
            self.cargo = cargo
        if salario is not None:
            self.salario = max(0, salario)
        if dependentes is not None:
            self.dependentes = max(0, dependentes)
        if beneficios is not None:
            self.beneficios = beneficios

    def dados_basicos(self):
        # Retorna os dados principais do colaborador em formato de dicionário
        return {
            "matricula": self.matricula,
            "nome": self.nome,
            "cargo": self.cargo,
            "salario": self.salario,
            "dependentes": self.dependentes,
            "beneficios": self.beneficios
        }

    def __str__(self):
        beneficios_str = ", ".join(self.beneficios) if self.beneficios else "Nenhum"
        return (
            f"Matrícula: {self.matricula} | "
            f"Nome: {self.nome} | "
            f"Cargo: {self.cargo} | "
            f"Salário: R$ {self.salario:.2f} | "
            f"Dependentes: {self.dependentes} | "
            f"Benefícios: {beneficios_str}"
        )