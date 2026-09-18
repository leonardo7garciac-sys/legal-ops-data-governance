# Referência de Prazos de Retenção — Departamento Jurídico

> **Aviso.** Este documento cobre as regras de prescrição, decadência e obrigação de guarda
> citadas no [RoPA](./ropa.md) da Corvina Software Ltda. Não é parecer jurídico nem fixa qual
> regra se aplica a um caso concreto — apenas registra, para cada norma citada no inventário, o
> que ela mede, o prazo nominal, a contagem e as causas de interrupção ou suspensão aplicáveis.

## Método

**1. Retenção não é prescrição.** O art. 16, LGPD, e seus incisos — taxativos — são o que
autoriza a conservação dos dados após o fim da finalidade do tratamento. A própria LGPD não fixa
por quanto tempo essa conservação pode durar. Quem mede esse tempo é a prescrição ou a decadência
da pretensão ou do direito que a hipótese do art. 16 invoca: o prazo prescricional ou
decadencial não autoriza nada por si só — ele mede a exposição da empresa, e é essa exposição
que determina por quanto tempo subsiste a obrigação invocada pelo art. 16.

**2. Interrupção e suspensão importam.** Um prazo prescricional interrompido recomeça do zero, e
um suspenso para de correr enquanto durar a causa da suspensão — em ambos os casos, a exposição
real se estende além do prazo nominal. Uma regra de retenção escrita como número fixo ("guardar
por 5 anos") está errada assim que uma ação é ajuizada, um processo apuratório é instaurado ou
qualquer outra causa de interrupção ou suspensão prevista em lei se manifesta.

**3. A contagem importa.** O termo inicial do prazo nem sempre coincide com o fim da relação que
gerou o documento. O art. 189, Código Civil, vincula o início da prescrição à violação do
direito, não ao encerramento do contrato ou da relação; o art. 173, I, Código Tributário
Nacional, inicia a contagem no primeiro dia do exercício seguinte àquele em que o lançamento
poderia ter sido efetuado, não na data do documento. Um prazo nominal de 5 anos raramente
corresponde a 5 anos corridos contados a partir do documento.

## Sumário

- [Método](#método)
- [Tabela de referência](#tabela-de-referência)
- [Lacunas](#lacunas)

## Tabela de referência

Uma linha por norma de retenção citada em qualquer atividade do RoPA. A coluna "O que mede"
distingue prescrição, decadência e obrigação de guarda — as três categorias não são
intercambiáveis. A coluna "Interrupção/suspensão" aponta para a norma que rege o tema, sem
detalhar cada causa individualmente.

| Norma | O que mede | Prazo nominal | Contagem | Interrupção/suspensão |
|---|---|---|---|---|
| art. 205, Código Civil | prescrição (regra residual) | 10 anos | art. 189, CC — da violação do direito | arts. 197 a 204, CC (impedimento, suspensão e interrupção); causas de interrupção listadas no art. 202, CC |
| art. 206, §3º, V, Código Civil | prescrição (reparação civil) | 3 anos | art. 189, CC — da violação do direito | arts. 197 a 204, CC; causas de interrupção no art. 202, CC |
| art. 206, §5º, I, Código Civil | prescrição (cobrança de dívida líquida constante de instrumento público ou particular) | 5 anos | art. 189, CC — da violação do direito | arts. 197 a 204, CC; causas de interrupção no art. 202, CC |
| art. 206-A, Código Civil | prescrição intercorrente | o mesmo prazo da pretensão de origem | corre durante a paralisação do processo, nos termos do art. 921, CPC — não há reinício automático do prazo ao fim da paralisação | sujeita às mesmas causas de impedimento, suspensão e interrupção (arts. 197 a 204, CC) e ao art. 921, CPC |
| art. 975, Código de Processo Civil | decadência (ação rescisória) | 2 anos | do trânsito em julgado da última decisão proferida no processo | art. 207, CC — decadência não se sujeita a impedimento, suspensão ou interrupção, ressalvada a exceção do art. 208, CC |
| art. 25, Lei 12.846/2013 | prescrição (pretensão punitiva) | 5 anos | a norma não especifica o marco inicial | parágrafo único do art. 25: interrompida pela instauração de processo administrativo ou judicial apto a apurar a infração |
| art. 174, Código Tributário Nacional | prescrição (cobrança do crédito tributário) | 5 anos | da constituição definitiva do crédito tributário | sujeita às causas de interrupção do parágrafo único do próprio art. 174, CTN |
| art. 195, parágrafo único, Código Tributário Nacional | obrigação de guarda (livros e comprovantes fiscais) | até a prescrição do crédito tributário a que se refere (art. 174, CTN) | prazo derivado — acompanha a contagem do art. 174, CTN | acompanha a interrupção/suspensão do crédito tributário a que se refere |
| art. 173, CTN / art. 173, I, CTN | decadência (constituição do crédito tributário) — registrado aqui explicitamente como **não sendo** regra de retenção documental | 5 anos | do primeiro dia do exercício seguinte àquele em que o lançamento poderia ter sido efetuado — antecipado, pelo parágrafo único do art. 173, CTN, para a data em que o sujeito passivo for notificado de medida preparatória indispensável ao lançamento, quando essa notificação anteceder o termo do caput | art. 207, CC — decadência não se sujeita a impedimento, suspensão ou interrupção, ressalvada a exceção do art. 208, CC |

## Lacunas

Prazos de retenção ainda marcados **[A DEFINIR]** no RoPA, e o que falta verificar em cada caso.

- **Ferramenta de intake jurídico.** Nem a hipótese do art. 16, LGPD, aplicável, nem o prazo
  estão definidos. As convenções do próprio projeto `legal-ops-intake` não definem uma política
  de retenção ou exclusão de dados. A verificar: se o projeto define, ou passa a definir, uma
  política própria de retenção.

- **Gestão de procurações e poderes.** Não foi identificada norma específica para o prazo de
  guarda após a revogação ou o término da vigência da procuração. A verificar: se há analogia
  defensável ao art. 205, Código Civil, ou se a empresa adota política interna própria — e, em
  qualquer caso, qual hipótese do art. 16, LGPD, se aplicaria.

- **Atendimento a requisições de titulares (arts. 18 a 22).** A LGPD não fixa prazo específico de
  guarda dos registros de atendimento a requisições. A verificar: eventual prazo definido em
  regulamento da ANPD, ou em política interna de comprovação de cumprimento — e a hipótese do
  art. 16, LGPD, aplicável.

- **Gestão de incidentes de segurança.** A Resolução CD/ANPD nº 15/2024 trata principalmente de
  prazos de comunicação do incidente, não de retenção dos registros. A verificar: eventual prazo
  definido em política interna, ou por analogia ao art. 206, Código Civil — e a hipótese do
  art. 16, LGPD, aplicável.
