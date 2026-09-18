# Comparativo LGPD × GDPR — Divergências com Efeito Operacional

> **Escopo.** Este documento não é uma visão geral das duas leis. Cobre apenas os pontos em que
> LGPD e GDPR divergem de um modo que muda o que uma empresa precisa efetivamente fazer —
> especificamente para uma empresa brasileira com clientes na Europa, como a Corvina Software
> Ltda. Não há conclusão sobre qual regime é mais rígido em geral; cada seção registra a
> divergência e o que ela significa na prática, sem comparar os regimes como um todo.

## Sumário

- [1. A obrigação de registro em si](#1-a-obrigação-de-registro-em-si)
- [2. Bases legais](#2-bases-legais)
- [3. Notificação de incidente](#3-notificação-de-incidente)
- [4. Transferência internacional](#4-transferência-internacional)
- [Por que isso importa para a Corvina](#por-que-isso-importa-para-a-corvina)

## 1. A obrigação de registro em si

**O que cada regime exige.** O art. 37, LGPD, impõe ao controlador e ao operador o dever de manter
registro das operações de tratamento de dados pessoais que realizarem, especialmente quando
baseadas no legítimo interesse — em uma única frase, sem incisos e sem detalhar o conteúdo mínimo
do registro. O art. 30, GDPR, é mais extenso: o art. 30(1) lista o conteúdo mínimo do registro do
controlador — identificação do controlador e, quando houver, do responsável conjunto pelo
tratamento, do representante e do encarregado; finalidades do tratamento; categorias de titulares
e de dados pessoais; categorias de destinatários; transferências internacionais para um terceiro
país ou organização internacional, incluindo a identificação desse terceiro país ou organização
e, no caso das transferências referidas no art. 49(1), segundo parágrafo, a documentação das
salvaguardas apropriadas; prazos previstos para a eliminação das diferentes categorias de dados,
quando possível; e, quando possível, uma descrição geral das medidas técnicas e organizacionais de
segurança referidas no art. 32(1) — e o art. 30(2) traz uma lista equivalente, porém mais
reduzida, para o operador. O art. 30(4) acrescenta que o registro deve ser disponibilizado à
autoridade de controle mediante solicitação; a LGPD não tem dispositivo expresso equivalente no
art. 37 — um fato sobre os dois textos, sem conclusão extraída dessa ausência.

**A isenção do art. 30(5), GDPR.** Organizações com menos de 250 empregados estão dispensadas do
registro do art. 30, GDPR, salvo se o tratamento que realizam (i) for suscetível de acarretar
risco aos direitos e liberdades dos titulares, (ii) não for ocasional, ou (iii) incluir categorias
especiais de dados (art. 9(1), GDPR) ou dados relacionados a condenações penais e infrações (art.
10, GDPR). A LGPD não prevê isenção equivalente — o art. 37 se aplica a todo controlador e
operador, independentemente do porte da organização ou do volume de tratamento.

**Efeito operacional.** Uma empresa com menos de 250 empregados pode estar dispensada do registro
sob o GDPR e, ainda assim, permanecer obrigada a mantê-lo sob a LGPD — a isenção de um regime não
dispensa do outro. E onde o GDPR define o conteúdo mínimo do registro artigo por artigo, a LGPD
deixa esse conteúdo em aberto: o formato e o nível de detalhe do registro brasileiro não decorrem
do texto do art. 37 em si. Do conteúdo mínimo do art. 30(1), duas das sete alíneas — a dos prazos
de eliminação (alínea "f") e a da descrição das medidas de segurança (alínea "g") — são
condicionadas, no próprio texto, por "se possível"; as demais alíneas não trazem essa
qualificação. Isso é registrado como um fato sobre o texto do art. 30(1), sem conclusão sobre se
isso aproxima ou afasta os dois regimes.

## 2. Bases legais

**Bases gerais — art. 7º, LGPD (dez hipóteses) × art. 6(1), GDPR (seis bases).**

| LGPD (art. 7º) | GDPR (art. 6(1)) | Correspondência |
|---|---|---|
| I — consentimento | (a) consentimento | direta |
| II — cumprimento de obrigação legal ou regulatória | (c) cumprimento de obrigação legal | direta |
| III — execução de políticas públicas pela administração pública | (e) execução de tarefa de interesse público ou exercício de autoridade pública | aproximada |
| IV — realização de estudos por órgão de pesquisa | — | sem base autônoma correspondente no art. 6(1); o GDPR trata pesquisa via art. 5(1)(b), art. 9(2)(j) e as derrogações do art. 89 |
| V — execução de contrato ou de procedimentos preliminares | (b) execução de contrato | direta |
| VI — exercício regular de direitos em processo judicial, administrativo ou arbitral (este último nos termos da Lei nº 9.307/1996, Lei de Arbitragem) | — | sem base autônoma correspondente; tratamento correlato costuma ser enquadrado em (f) legítimo interesse |
| VII — proteção da vida ou da incolumidade física do titular ou de terceiro | (d) proteção de interesses vitais | direta, mas ver a nota sobre a cisão VII/VIII abaixo |
| VIII — tutela da saúde, exclusivamente por profissionais/serviços de saúde ou autoridade sanitária | — | sem base autônoma no art. 6(1); o GDPR trata tratamento de dados de saúde como exceção do art. 9(2), não como base geral do art. 6 |
| IX — interesses legítimos do controlador ou de terceiro | (f) legítimos interesses | direta |
| X — proteção do crédito | — | sem correspondente no art. 6(1) |

A LGPD separa proteção da vida (VII) de tutela da saúde (VIII) como duas hipóteses distintas; o
GDPR não replica essa cisão no art. 6(1) — a base de interesses vitais (art. 6(1)(d)) é genérica,
e o tratamento de dados de saúde propriamente dito é endereçado no art. 9(2), não no art. 6.

**Dados sensíveis — art. 11, LGPD × art. 9(2), GDPR.**

O inciso II do art. 11 é uma única hipótese, não sete: aplica-se, no seu caput, "sem fornecimento
de consentimento do titular, nas hipóteses em que for indispensável para" as situações descritas
nas alíneas "a" a "g" abaixo — que são formas dessa hipótese única, não hipóteses autônomas, no
mesmo padrão já registrado para o art. 33, II, LGPD, na Seção 4. O art. 9(2), GDPR, não tem um
caput equivalente: cada uma de suas exceções, de (a) a (j), carrega as próprias condições, sem um
requisito comum de indispensabilidade que as una. Isso é registrado como uma divergência com
efeito operacional — a avaliação de indispensabilidade sob a LGPD é feita uma vez, sob o padrão
comum do caput do inciso II, enquanto sob o GDPR cada exceção do art. 9(2) precisa ser avaliada
segundo suas próprias condições — e não como uma conclusão sobre qual regime é mais rígido.

| LGPD (art. 11) | GDPR (art. 9(2)) | Correspondência |
|---|---|---|
| I — consentimento específico e destacado | (a) consentimento explícito | direta |
| II, "a" — cumprimento de obrigação legal ou regulatória pelo controlador | (b) obrigações e direitos específicos do controlador ou do titular no domínio do direito do trabalho e da segurança e proteção social | parcial — a exceção do GDPR é restrita ao contexto trabalhista/previdenciário; a da LGPD é geral |
| II, "b" — tratamento compartilhado para execução de políticas públicas | (g) razões de interesse público importante | aproximada |
| II, "c" — estudos por órgão de pesquisa, com anonimização garantida | (j) arquivamento de interesse público, pesquisa científica/histórica ou fins estatísticos | aproximada |
| II, "d" — exercício regular de direitos, inclusive em contrato e em processo judicial, administrativo e arbitral | (f) exercício ou defesa de direito em processo judicial ou sempre que os tribunais atuem no exercício de sua função jurisdicional | aproximada |
| II, "e" — proteção da vida ou da incolumidade física do titular ou de terceiro | (c) proteção de interesses vitais, caso o titular esteja física ou legalmente incapaz de consentir | parcial — o GDPR condiciona a exceção à incapacidade de consentir; a LGPD não impõe essa condição |
| II, "f" — tutela da saúde, por profissionais/serviços de saúde ou autoridade sanitária | (h) medicina preventiva ou do trabalho, diagnóstico médico, prestação de cuidados de saúde ou de ação social | direta quanto ao núcleo, aproximada quanto ao detalhamento |
| II, "g" — prevenção à fraude e à segurança do titular em identificação/autenticação | — | sem correspondente direto no art. 9(2) |
| — | (d) atividades legítimas de fundação, associação ou organismo sem fins lucrativos, de finalidade política, filosófica, religiosa ou sindical, quanto a seus membros | sem correspondente direto no art. 11 |
| — | (e) dados manifestamente tornados públicos pelo titular | sem correspondente direto no art. 11 |
| — | (i) saúde pública | sem hipótese autônoma separada no art. 11 (tratada dentro da tutela da saúde, II, "f") |

**Efeito operacional.** Um tratamento estruturado sobre pesquisa (art. 7º, IV), exercício de
direitos fora de processo (art. 7º, VI) ou proteção ao crédito (art. 7º, X) perde sua base
autônoma assim que passa a alcançar titulares na União Europeia — é preciso reenquadrá-lo em uma
das seis bases do art. 6(1), quando isso for possível. O mesmo vale, para dados sensíveis, com a
base de prevenção à fraude do art. 11, II, "g". Na direção inversa, hipóteses do art. 9(2), GDPR,
sem correspondente na LGPD (atividades de organizações sem fins lucrativos, dados manifestamente
públicos) não suprem, isoladamente, a necessidade de uma base do art. 11 para o mesmo tratamento
no Brasil.

## 3. Notificação de incidente

**GDPR — prazo fixo de 72 horas.** O art. 33(1), GDPR, exige que o controlador comunique a
autoridade de controle competente "sem demora injustificada e, sempre que possível, no prazo de
72 horas após ter tomado conhecimento" da violação de dados pessoais, salvo se for improvável que
a violação represente risco para os direitos e liberdades das pessoas singulares. O art. 33(3)
lista o conteúdo mínimo dessa comunicação. Já a comunicação ao titular, quando a violação for
suscetível de gerar risco elevado, segue o art. 34(1) — "sem demora injustificada", sem um número
fixo de horas equivalente ao prazo do art. 33(1). O gatilho, em ambos os casos, é o momento em
que o controlador toma conhecimento do incidente.

**LGPD — prazo fixado pela Resolução CD/ANPD nº 15/2024.** O art. 48, caput, LGPD, impõe ao
controlador o dever de comunicar à autoridade nacional e ao titular a ocorrência de incidente de
segurança que possa acarretar risco ou dano relevante aos titulares. O próprio texto legal não
fixa um número de dias ou horas: o art. 48, §1º, remete essa definição a "prazo razoável, conforme
definido pela autoridade nacional". A Resolução CD/ANPD nº 15/2024 fixa esse prazo em 3 (três)
dias úteis, em dois dispositivos separados: o art. 6º trata da comunicação à ANPD, e o art. 9º, da
comunicação ao titular. Em ambos os casos, a contagem começa quando o controlador toma
conhecimento de que o incidente afetou dados pessoais — não a partir da ocorrência do incidente em
si. A própria Resolução prevê dois ajustes a esse prazo: agentes de tratamento de pequeno porte
têm o prazo dobrado, tanto para a comunicação à ANPD (art. 6º, §8º) quanto para a comunicação ao
titular (art. 9º, §6º); e, além da comunicação inicial, um relatório complementar é devido à ANPD
no prazo de 20 (vinte) dias úteis.

**Efeito operacional.** Um único incidente que atinja titulares no Brasil e na União Europeia roda
em dois relógios diferentes, com dois gatilhos que podem não coincidir: o GDPR conta a partir do
momento em que o controlador toma conhecimento da violação, com um teto fixo de 72 horas corridas
para a comunicação à autoridade; a LGPD conta a partir do momento em que o controlador toma
conhecimento de que o incidente afetou dados pessoais, com um teto de 3 dias úteis. Como o prazo
brasileiro corre em dias úteis e o europeu em horas corridas, os 3 dias úteis da Resolução CD/ANPD
nº 15/2024 podem corresponder a 5 ou 6 dias corridos, a depender de fins de semana e feriados no
intervalo — os dois prazos não são diretamente comparáveis em horas.

## 4. Transferência internacional

**GDPR — Capítulo V.** A regra geral do art. 44 condiciona qualquer transferência internacional
ao cumprimento das condições do próprio Capítulo V. Os mecanismos são: decisão de adequação da
Comissão Europeia (art. 45); transferências mediante garantias apropriadas (art. 46), incluindo
duas vias de cláusulas-padrão — art. 46(2)(c), cláusulas-padrão de proteção de dados adotadas pela
própria Comissão Europeia, e art. 46(2)(d), cláusulas-padrão de proteção de dados adotadas por uma
autoridade de controle e aprovadas pela Comissão Europeia — além de normas corporativas
vinculantes (art. 47); e derrogações para situações
específicas (art. 49), como consentimento explícito, necessidade para execução de contrato, razões
importantes de interesse público, exercício de direito em processo judicial, ou proteção de
interesses vitais.

**LGPD — art. 33.** O art. 33, LGPD, lista nove hipóteses que legitimam a transferência
internacional de dados pessoais:

| Inciso | Hipótese |
|---|---|
| I | decisão de adequação — países ou organismos internacionais que proporcionem grau de proteção de dados pessoais adequado ao previsto na LGPD |
| II | dever de o controlador oferecer e comprovar garantias de cumprimento dos princípios, dos direitos do titular e do regime de proteção de dados previstos na LGPD, por meio de: "a" — cláusulas contratuais específicas para uma determinada transferência; "b" — cláusulas-padrão contratuais; "c" — normas corporativas globais; "d" — selos, certificados e códigos de conduta regularmente emitidos |
| III | cooperação jurídica internacional entre órgãos públicos de inteligência, investigação e persecução |
| IV | proteção da vida ou da incolumidade física do titular ou de terceiro |
| V | autorização da ANPD |
| VI | compromisso assumido em acordo de cooperação internacional |
| VII | execução de política pública ou atribuição legal de serviço público |
| VIII | consentimento específico e destacado do titular, com informação prévia sobre o caráter internacional da operação, distinguida claramente das demais finalidades |
| IX | necessidade de atender às hipóteses dos incisos II, V e VI do art. 7º (cumprimento de obrigação legal, execução de contrato e exercício regular de direitos em processo) |

O inciso II é uma única hipótese, não quatro — o dever de oferecer e comprovar garantias — e suas
alíneas "a" a "d" são as formas que essa garantia pode assumir, não hipóteses autônomas. A alínea
"a" (cláusulas contratuais específicas para determinada transferência) é distinta da alínea "b"
(cláusulas-padrão contratuais, de aplicação genérica) — a Resolução CD/ANPD nº 19/2024 aprovou
especificamente o instrumento da alínea "b".

Como observação estrutural: a forma do inciso II — um caput que impõe o dever de garantia, seguido
de uma lista de instrumentos que a satisfazem — tem um paralelo com a estrutura do art. 46, GDPR:
o art. 46(1) impõe a exigência de garantias apropriadas, e o art. 46(2) lista os instrumentos que
a satisfazem. Isso é registrado como um fato sobre a forma dos dois dispositivos, não como uma
conclusão sobre a equivalência entre eles.

**A aproximação trazida pela Resolução CD/ANPD nº 19/2024.** Essa Resolução aprovou as
cláusulas-padrão contratuais brasileiras — o instrumento do art. 33, II, "b", LGPD — e o
regulamento de transferência internacional de dados pessoais no âmbito da LGPD. Esse é o fato
registrado aqui: a Resolução adotou, como mecanismo operacional para a garantia exigida pelo art.
33, II, LGPD, o mesmo tipo de instrumento — cláusulas-padrão contratuais — que o art. 46, GDPR, já
usa como uma de suas vias de garantias apropriadas. O art. 46(2)(d), GDPR, especificamente, trata de
cláusulas-padrão adotadas por uma autoridade de controle da União e aprovadas pela Comissão
Europeia — a semelhança estrutural entre esse mecanismo e cláusulas-padrão adotadas por uma
autoridade nacional, como a ANPD, é institucional (autoridade que adota, cláusulas que passam por
aprovação), não uma questão de as cláusulas brasileiras se enquadrarem nesse sub-parágrafo do
GDPR. Isso é registrado como fato sobre os dois mecanismos, não como uma conclusão sobre se as
cláusulas-padrão brasileiras satisfazem o Capítulo V, GDPR.

**Efeito operacional.** Uma transferência de dados entre a Corvina e um cliente ou fornecedor na
União Europeia precisa de um mecanismo legitimador em cada ponta: do lado brasileiro, uma das
hipóteses do art. 33, LGPD; do lado europeu, uma das vias do Capítulo V, GDPR. A adoção de
cláusulas-padrão contratuais brasileiras pela Resolução CD/ANPD nº 19/2024 aproxima os dois
mecanismos operacionalmente, mas não os torna automaticamente intercambiáveis — cada regime
continua a exigir que a hipótese aplicável em seu próprio texto esteja satisfeita. O art. 33, IX,
LGPD, não é uma hipótese autônoma de transferência: ele remete de volta às hipóteses dos incisos
II, V e VI do art. 7º, já tratadas na Seção 2 — uma transferência fundamentada no inciso IX
depende, portanto, de a base subjacente do art. 7º efetivamente se sustentar, o que liga
diretamente esta seção à análise de bases legais feita acima. Este documento não conclui qual
hipótese do art. 33 ou do Capítulo V, GDPR, se aplicaria a uma transferência concreta da Corvina.

## Por que isso importa para a Corvina

A Corvina Software Ltda. é uma empresa brasileira de B2B SaaS. Sua base de clientes na Europa é
uma premissa introduzida neste documento, e não em `docs/ropa.md` ou nos projetos irmãos
`legal-ops-contract-analytics` e `legal-ops-intake`, que não descrevem o mercado ou a base de
clientes da empresa. Assumida essa premissa, a Corvina fica sob os dois regimes ao mesmo tempo.

**Os dois regimes têm alcance territorial e extraterritorial — não apenas um deles.** O caput do
art. 3º, LGPD, dispõe que a lei se aplica independentemente do país onde esteja sediada a entidade
ou onde estejam localizados os dados, desde que se verifique uma das hipóteses de seus três
incisos. O inciso I é a hipótese territorial propriamente dita — "a operação de tratamento seja
realizada no território nacional". Os incisos II e III são, eles próprios, hipóteses de alcance
extraterritorial: o inciso II alcança a operação cujo objetivo seja a oferta ou o fornecimento de
bens ou serviços, ou o tratamento de dados de indivíduos localizados no território nacional; o
inciso III alcança os dados pessoais coletados no território nacional, com o §1º definindo a
coleta pelo local em que se encontrava o titular no momento da coleta. A Corvina se enquadra no
art. 3º, I, LGPD — por realizar a operação de tratamento em território nacional — e não porque a
LGPD se limite ao território: a lei tem, ela própria, hipóteses de alcance extraterritorial nos
incisos II e III, que não são o fundamento da aplicação à Corvina.

O GDPR segue a mesma lógica de dupla via. O art. 3(1) é sua hipótese territorial, aplicável ao
tratamento realizado no contexto das atividades de um estabelecimento do controlador ou operador
na União, independentemente de o tratamento ocorrer ou não na própria União. O art. 3(2)(a) é a
via extraterritorial, que alcança o controlador não estabelecido na União quando o tratamento
estiver relacionado à oferta de bens ou serviços a titulares de dados na União, independentemente
de pagamento. É essa segunda via que alcança a Corvina, que não está estabelecida na União.

**Uma hipótese de exclusão a registrar.** O art. 4º, IV, LGPD, exclui do âmbito de aplicação da
lei os dados pessoais provenientes de fora do território nacional que não sejam objeto de
comunicação, de uso compartilhado com agentes de tratamento brasileiros, ou de transferência
internacional de dados com outro país que não o de proveniência, desde que o país de proveniência
proporcione grau de proteção de dados pessoais adequado ao previsto na LGPD. Essa é uma hipótese
relevante para uma empresa brasileira que recebe dados de origem europeia — registrada aqui como
regra, sem conclusão sobre se ela alcança algum tratamento específico da Corvina.
