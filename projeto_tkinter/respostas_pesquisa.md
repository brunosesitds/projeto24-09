# Respostas da pesquisa sobre Tkinter

1. O que é Tkinter e qual é sua relação com Python e Tcl/Tk?

Tkinter é a biblioteca padrão de interfaces gráficas (GUI) do Python, que fornece bindings para a toolkit Tcl/Tk. Tcl/Tk é uma biblioteca C para criação de interfaces; o Python expõe suas funcionalidades via Tkinter permitindo construir janelas, widgets e tratar eventos diretamente em código Python.

2. O que caracteriza uma aplicação orientada a eventos? Explique o papel do `mainloop`.

Aplicações orientadas a eventos permanecem em espera por eventos (cliques, teclas, timers) e reagem por meio de callbacks. O `mainloop` é o laço principal que processa eventos e atualiza a interface; sem ele a janela não responde.

3. O que são widgets? Descreva `Label`, `Entry`, `Button`, `Frame`, `Text`, `Checkbutton`, `Radiobutton`, `Combobox` e `Treeview`/`Listbox`.

- `Label`: exibe texto ou imagem não editável.
- `Entry`: campo de texto de linha única para entrada curta.
- `Button`: botão clicável que aciona uma ação.
- `Frame`: contêiner para agrupar outros widgets e organizar layout.
- `Text`: área de texto multilinha; permite edição rica.
- `Checkbutton`: caixa de seleção (on/off).
- `Radiobutton`: opção exclusiva dentro de um grupo.
- `Combobox` (ttk): lista suspensa para seleção única com entrada opcional.
- `Treeview`/`Listbox`: exibe listas/tabelas; `Treeview` permite colunas e hierarquia.

4. Compare os gerenciadores de geometria `pack`, `grid` e `place`. Quando usar cada um?

- `pack`: fácil para layouts simples (pilhas vertical/horizontal).
- `grid`: grade flexível para alinhamento por linhas/colunas; recomendado para formulários.
- `place`: posicionamento absoluto (coordenadas); útil para layouts personalizados mas menos responsivo.

5. O que são callbacks e como eventos de clique, teclado ou seleção podem chamar funções?

Callbacks são funções registradas para serem chamadas quando ocorre um evento. Em Tkinter associa-se funções a eventos via `command=` em widgets ou `bind()` para eventos específicos como `<Button-1>` ou `<Key>`.

6. Para que servem `StringVar`, `IntVar`, `DoubleVar` e `BooleanVar`?

São classes de variáveis vinculáveis que mantêm estado sincronizado entre widgets e código, facilitando leitura/escrita e permitindo rastrear mudanças via `.trace()`.

7. Como validar campos obrigatórios, números, datas e valores dentro de limites?

Validações podem ser feitas tanto ao submeter o formulário quanto usando validação em tempo real (`validate`/`validatecommand`) no `Entry`. Converter e checar tipos (int/float), usar regex para formatos de data e verificar intervalos numéricos. Informar o usuário com `messagebox`.

8. Como utilizar `messagebox`, `filedialog` e `ttk` para melhorar interação e aparência?

`messagebox` mostra alertas, confirmações e erros; `filedialog` facilita abrir/salvar arquivos com diálogo nativo; `ttk` fornece widgets com aparência nativa e temas, melhorando a usabilidade.

9. Quais formas de persistência podem ser usadas? Compare JSON, CSV e SQLite.

- JSON: leve e legível; bom para estruturas hierárquicas; não é ideal para consultas complexas.
- CSV: para tabelas simples; fácil interoperabilidade com planilhas; sem tipos complexos.
- SQLite: banco relacional embutido; suporta consultas, transações e integridade; recomendado para aplicações com múltiplos registros e necessidades de busca/filtragem.

10. Quais cuidados de usabilidade e acessibilidade devem existir em uma interface desktop?

Organização visual clara, rótulos descritivos, feedback imediato em ações, validação e mensagens compreensíveis, atalhos de teclado, foco visível, contraste adequado e compatibilidade com leitores de tela quando possível.

11. Quais são as vantagens e limitações do Tkinter em relação a outras opções?

Vantagens: parte da biblioteca padrão, leve, simples para aplicações pequenas/educacionais, amplamente documentado. Limitações: aparência menos moderna comparado a toolkits mais recentes (Qt, Electron), menos recursos nativos avançados e menor ecossistema de componentes prontos.

12. Como distribuir ou executar o aplicativo em outro computador? Cite dependências e cuidados.

Podem ser distribuídos o código Python acompanhado de instruções (README) e dependências; para criar executáveis usar `pyinstaller` ou `cx_Freeze`. Cuidados: testar em sistemas alvo, incluir arquivos de dados (banco), tratar caminhos relativos, e documentar requisitos de versão do Python.
