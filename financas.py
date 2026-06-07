class Financas:

    VALOR_BENEFICIOS = {
        "Vale Transporte": 200,
        "Vale Refeição": 400,
        "Plano de Saúde": 600
    }

    def __init__(self, colaborador):
        self.colaborador = colaborador

    # -------------------------
    # INSS (PROGRESSIVO)
    # -------------------------

    def calcular_inss(self) -> float:

        salario = self.colaborador.salario

        faixas = [
            (1320.00, 0.075),
            (2571.29, 0.09),
            (3856.94, 0.12),
            (7507.49, 0.14)
        ]

        total_inss = 0
        limite_anterior = 0

        for limite, aliquota in faixas:

            if salario > limite:

                total_inss += (
                    (limite - limite_anterior)
                    * aliquota
                )

                limite_anterior = limite

            else:

                total_inss += (
                    (salario - limite_anterior)
                    * aliquota
                )

                return total_inss

        return total_inss

    # -------------------------
    # IRRF
    # -------------------------

    def calcular_irrf(self) -> float:

        salario = self.colaborador.salario
        inss = self.calcular_inss()
        dependentes = self.colaborador.dependentes

        base_calculo = (
            salario
            - inss
            - (dependentes * 189.59)
        )

        if base_calculo <= 2112:
            return 0

        elif base_calculo <= 2826.65:
            return max(
                0,
                (base_calculo * 0.075) - 158.40
            )

        elif base_calculo <= 3751.05:
            return max(
                0,
                (base_calculo * 0.15) - 370.40
            )

        elif base_calculo <= 4664.68:
            return max(
                0,
                (base_calculo * 0.225) - 651.73
            )

        else:
            return max(
                0,
                (base_calculo * 0.275) - 884.96
            )

    # -------------------------
    # FGTS
    # -------------------------

    def calcular_fgts(self) -> float:

        return self.colaborador.salario * 0.08

    # -------------------------
    # BENEFÍCIOS
    # -------------------------

    def calcular_total_beneficios(self) -> float:

        return sum(
            self.VALOR_BENEFICIOS.get(
                beneficio,
                0
            )
            for beneficio in self.colaborador.beneficios
        )

    # -------------------------
    # FÉRIAS
    # -------------------------

    def calcular_ferias(self):

        salario = self.colaborador.salario

        um_terco = salario / 3

        total_ferias = salario + um_terco

        return (
            salario,
            um_terco,
            total_ferias
        )

    # -------------------------
    # SALÁRIO LÍQUIDO
    # -------------------------

    def calcular_salario_liquido(self) -> float:

        salario = self.colaborador.salario

        inss = self.calcular_inss()

        irrf = self.calcular_irrf()

        beneficios = self.calcular_total_beneficios()

        return (
            salario
            - inss
            - irrf
            + beneficios
        )

    # -------------------------
    # CUSTO EMPRESA
    # -------------------------

    def calcular_custo_empresa(self) -> float:

        salario = self.colaborador.salario

        fgts = self.calcular_fgts()

        beneficios = self.calcular_total_beneficios()

        return (
            salario
            + fgts
            + beneficios
        )

    # -------------------------
    # HOLERITE
    # -------------------------

    def gerar_holerite(self) -> str:

        bruto = self.colaborador.salario

        inss = self.calcular_inss()

        irrf = self.calcular_irrf()

        fgts = self.calcular_fgts()

        beneficios_valor = (
            self.calcular_total_beneficios()
        )

        liquido = self.calcular_salario_liquido()

        custo_empresa = (
            self.calcular_custo_empresa()
        )

        (
            salario_ferias,
            um_terco,
            total_ferias
        ) = self.calcular_ferias()

        beneficios_lista = (
            ", ".join(self.colaborador.beneficios)
            if self.colaborador.beneficios
            else "Nenhum"
        )

        return f"""
================= HOLERITE =================

Matrícula: {self.colaborador.matricula}
Nome: {self.colaborador.nome}
Cargo: {self.colaborador.cargo}
Número de Dependentes: {self.colaborador.dependentes}

----------- SALÁRIO -----------
Salário Bruto: R$ {bruto:.2f}

----------- ENCARGOS ----------
INSS: R$ {inss:.2f}
IRRF: R$ {irrf:.2f}
FGTS (8%): R$ {fgts:.2f}

----------- BENEFÍCIOS --------
Benefícios:
{beneficios_lista}

Total Benefícios: R$ {beneficios_valor:.2f}

----------- FÉRIAS ------------
Salário Férias: R$ {salario_ferias:.2f}
1/3 Constitucional: R$ {um_terco:.2f}
Total Férias: R$ {total_ferias:.2f}

------ CUSTO PARA EMPRESA -----
Custo Mensal do Funcionário: R$ {custo_empresa:.2f}

===================================
Salário Líquido: R$ {liquido:.2f}
===================================
"""