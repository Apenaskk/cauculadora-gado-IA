import streamlit as st
import pandas as pd

# Configuração da página do aplicativo
st.set_page_config(
    page_title="Gestão Inteligente de Lotes - Pecuária",
    page_icon="🐂",
    layout="centered"
)

# Estilo visual limpo e profissional
st.title("🐂 Calculadora e Analisadora de Lotes de Gado")
st.markdown("Insira os pesos do lote e selecione a categoria para obter métricas instantâneas e um parecer técnico automatizado.")

# 1. Painel Lateral ou Seção de Parâmetros do Lote
st.sidebar.header("⚙️ Configurações do Lote")
categoria_lote = st.sidebar.selectbox(
    "Categoria Animal:",
    [
        "Recria / Desmama (6 a 12 meses)",
        "Crescimento / Garrote (12 a 24 meses)",
        "Terminação / Engorda Final (> 24 meses)"
    ]
)

# 2. Entrada dos Pesos na Interface Principal
st.subheader("📝 Entrada de Dados")
entrada_pesos = st.text_area(
    "Digite os pesos dos animais (separados por vírgula):",
    placeholder="Ex: 450, 480, 510, 430, 465, 490",
    help="Cole ou digite todos os pesos individuais obtidos na pesagem do lote."
)

# 3. Botão de Processamento Principal
if st.button("🚀 Processar e Analisar Lote", type="primary"):
    if entrada_pesos:
        try:
            # Tratamento de dados robusto (converte texto em lista numérica e limpa espaços)
            pesos = [float(p.strip()) for p in entrada_pesos.split(",") if p.strip()]

            if len(pesos) > 0:
                # Transformando em DataFrame para análises avançadas com Pandas
                df = pd.DataFrame(pesos, columns=["Peso"])

                # Cálculos estatísticos precisos
                total_animais = int(len(df))
                peso_total = float(df["Peso"].sum())
                peso_medio = float(df["Peso"].mean())
                peso_max = float(df["Peso"].max())
                peso_min = float(df["Peso"].min())
                amplitude = peso_max - peso_min  # Indicador de desuniformidade do lote

                st.success("Processamento concluído com sucesso!")

                # Exibindo Métricas Visuais em Cartões
                st.subheader("📊 Indicadores Estatísticos do Lote")
                col1, col2, col3 = st.columns(3)
                col1.metric("Total de Animais", f"{total_animais}")
                col2.metric("Peso Médio", f"{peso_medio:.2f} kg")
                col3.metric("Peso Total", f"{peso_total:,.2f} kg".replace(",", "."))

                col4, col5, col6 = st.columns(3)
                col4.metric("Maior Peso", f"{peso_max:.2f} kg")
                col5.metric("Menor Peso", f"{peso_min:.2f} kg")
                col6.metric("Amplitude (Desvio)", f"{amplitude:.2f} kg", help="Diferença entre o boi mais pesado e o mais leve.")

                # Gráfico nativo limpo e direto
                st.subheader("📈 Distribuição Visual dos Pesos")
                st.bar_chart(df["Peso"])

                # Motor de Análise Inteligente e Diagnóstico Automatizado
                st.subheader("🤖 Diagnóstico Técnico Automatizado")

                diagnostico = ""
                alerta_uniformidade = ""

                # Avaliando uniformidade do lote (amplitude alta indica lote desuniforme)
                if amplitude > 100:
                    alerta_uniformidade = "⚠️ **Atenção à Uniformidade:** A amplitude entre o animal mais leve e o mais pesado é superior a 100 kg. Recomenda-se separar os lotes para evitar competição no cocho."
                else:
                    alerta_uniformidade = "✅ **Boa Uniformidade:** O lote apresenta boa padronização de pesos, facilitando o manejo alimentar."

                # Regras inteligentes cruzadas com a categoria
                if "Recria" in categoria_lote:
                    if peso_medio < 220:
                        diagnostico = f"O lote está em fase inicial de recria com média de {peso_medio:.1f}kg. O desenvolvimento está abaixo do potencial esperado para a idade, exigindo revisão da pastagem ou suplementação proteica."
                    else:
                        diagnostico = f"Lote em recria apresentando excelente desempenho ponderal (média de {peso_medio:.1f}kg). Boa adaptação e estrutura corporal em desenvolvimento."

                elif "Crescimento" in categoria_lote:
                    if peso_medio < 350:
                        diagnostico = f"Garrotes na faixa de crescimento com média de {peso_medio:.1f}kg. Ritmo de ganho de peso moderado; avaliar ajuste de minerais e volumoso."
                    else:
                        diagnostico = f"Otimo rendimento na fase de crescimento, registrando média de {peso_medio:.1f}kg. Animais respondendo bem ao plano nutricional atual."

                elif "Terminação" in categoria_lote:
                    if peso_medio < 480:
                        diagnostico = f"Lote em terminação com média de {peso_medio:.1f}kg. Ainda necessita de tempo de cocho (engorda intensiva) para atingir o peso ideal de abate comercial."
                    else:
                        diagnostico = f"🎯 **Ponto de Abate Atingido!** Lote pronto para comercialização, com média de peso excepcional de {peso_medio:.1f}kg."

                # Exibindo os blocos de texto estilizados
                st.info(diagnostico)
                if alerta_uniformidade:
                    st.warning(alerta_uniformidade)

            else:
                st.warning("Por favor, insira pelo menos um peso válido.")

        except ValueError:
            st.error("Erro de formato: Certifique-se de digitar apenas números separados por vírgula (Ex: 450, 480, 510). Evite letras ou caracteres especiais.")
    else:
        st.warning("O campo de pesos está vazio. Insira os dados para gerar o relatório.")
else:
    st.info("💡 **Dica:** Digite ou cole os valores no campo acima e clique em 'Processar e Analisar Lote' para ver os resultados.")
