class Financas:

    VALOR_BENEFICIOS = {
        "Vale Transporte": 200,
        "Vale Refeição": 400,
        "Plano de Saúde": 600
    }

    def __init__(self, colaborador):
        self.colaborador = colaborador

    def calcular_inss(self):
        salario = self.colaborador.salario

        if salario <= 1320:
            return salario * 0.075
        elif salario <= 2571.29:
            return salario * 0.09
        elif salario <= 3856.94:
            return salario * 0.12
        else:
            return salario * 0.14

    def calcular_irrf(self):
        salario = self.colaborador.salario
        inss = self.calcular_inss()
        dependentes = self.colaborador.dependentes

        base = salario - inss - (dependentes * 189.59)

        if base <= 2112:
            return 0
        elif base <= 2826.65:
            return base * 0.075 - 158.40
        elif base <= 3751.05:
            return base * 0.15 - 370.40
        elif base <= 4664.68:
            return base * 0.225 - 651.73
        else:
            return base * 0.275 - 884.96

    def calcular_fgts(self):
        return self.colaborador.salario * 0.08

    def calcular_total_beneficios(self):
        total = 0
        for beneficio in self.colaborador.beneficios:
            total += self.VALOR_BENEFICIOS.get(beneficio, 0)
        return total

    def calcular_ferias(self):
        salario = self.colaborador.salario
        um_terco = salario / 3
        total_ferias = salario + um_terco
        return salario, um_terco, total_ferias

    def calcular_salario_liquido(self):
        salario = self.colaborador.salario
        inss = self.calcular_inss()
        irrf = self.calcular_irrf()
        beneficios = self.calcular_total_beneficios()

        return salario - inss - irrf + beneficios

    def gerar_holerite(self):
        bruto = self.colaborador.salario
        inss = self.calcular_inss()
        irrf = self.calcular_irrf()
        fgts = self.calcular_fgts()
        beneficios = self.calcular_total_beneficios()
        liquido = self.calcular_salario_liquido()

        salario_ferias, um_terco, total_ferias = self.calcular_ferias()

        beneficios_lista = ", ".join(self.colaborador.beneficios) if self.colaborador.beneficios else "Nenhum"

        return f"""
================= HOLERITE =================
Matrícula: {self.colaborador.matricula}
Nome: {self.colaborador.nome}
Cargo: {self.colaborador.cargo}
Dependentes: {self.colaborador.dependentes}

----------- SALÁRIO -----------
Salário Bruto: R$ {bruto:.2f}

----------- ENCARGOS -----------
INSS: R$ {inss:.2f}
IRRF: R$ {irrf:.2f}
FGTS (8%): R$ {fgts:.2f}

----------- BENEFÍCIOS ----------
{beneficios_lista}
Total Benefícios: R$ {beneficios:.2f}

----------- FÉRIAS --------------
Salário Férias: R$ {salario_ferias:.2f}
1/3 Constitucional: R$ {um_terco:.2f}
Total Férias: R$ {total_ferias:.2f}

===================================
Salário Líquido: R$ {liquido:.2f}
===================================
"""
