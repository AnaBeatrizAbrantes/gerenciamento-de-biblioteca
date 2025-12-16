let livros = [];
let emprestimos = [];

function mostrarSecao(id) {
  document
    .querySelectorAll(".secao")
    .forEach((sec) => sec.classList.remove("ativa"));
  document.getElementById(id).classList.add("ativa");
}

document.getElementById("formCadastro").addEventListener("submit", (e) => {
  e.preventDefault();
  const titulo = document.getElementById("titulo").value;
  const autor = document.getElementById("autor").value;
  const ano = document.getElementById("ano").value;

  livros.push({ titulo, autor, ano, disponivel: true });
  document.getElementById("mensagem").innerText =
    "Livro cadastrado com sucesso!";

  document.getElementById("formCadastro").reset();
  atualizarLista();
});

function atualizarLista() {
  const ul = document.getElementById("listaLivros");
  ul.innerHTML = "";
  livros.forEach((livro) => {
    const status = livro.disponivel ? "Disponível" : "Emprestado";
    ul.innerHTML += `<li><strong>${livro.titulo}</strong> - ${livro.autor} (${livro.ano}) <em>${status}</em></li>`;
  });
}

function buscarLivro() {
  const termo = document.getElementById("buscaInput").value.toLowerCase();
  const resultados = livros.filter((l) =>
    l.titulo.toLowerCase().includes(termo)
  );
  const ul = document.getElementById("resultadoBusca");
  ul.innerHTML =
    resultados.length > 0
      ? resultados.map((l) => `<li>${l.titulo} - ${l.autor}</li>`).join("")
      : "<li>Nenhum livro encontrado.</li>";
}

document.getElementById("formEmprestimo").addEventListener("submit", (e) => {
  e.preventDefault();
  const titulo = document.getElementById("tituloEmprestimo").value;
  const usuario = document.getElementById("usuarioEmprestimo").value;
  const dias = parseInt(document.getElementById("diasEmprestimo").value);

  const livro = livros.find(
    (l) => l.titulo.toLowerCase() === titulo.toLowerCase()
  );
  const msg = document.getElementById("mensagemEmprestimo");

  if (!livro) {
    msg.innerText = "Livro não encontrado!";
    return;
  }
  if (!livro.disponivel) {
    msg.innerText = "Esse livro já está emprestado!";
    return;
  }

  livro.disponivel = false;
  emprestimos.push({ titulo: livro.titulo, usuario, dias });
  msg.innerText = `Livro '${livro.titulo}' emprestado para ${usuario} por ${dias} dias!`;

  document.getElementById("formEmprestimo").reset();
  atualizarLista();
  atualizarEmprestimos();
});

function atualizarEmprestimos() {
  const ul = document.getElementById("listaEmprestimos");
  ul.innerHTML = "";

  if (emprestimos.length === 0) {
    ul.innerHTML = "<li>Nenhum empréstimo ativo.</li>";
    return;
  }

  emprestimos.forEach((e) => {
    ul.innerHTML += `<li><strong>${e.titulo}</strong> → ${e.usuario} (${e.dias} dias)</li>`;
  });
}

function devolverLivro() {
  const titulo = document.getElementById("tituloDevolucao").value.toLowerCase();
  const msg = document.getElementById("mensagemEmprestimo");

  const indexEmp = emprestimos.findIndex(
    (e) => e.titulo.toLowerCase() === titulo
  );
  const livro = livros.find((l) => l.titulo.toLowerCase() === titulo);

  if (indexEmp === -1 || !livro) {
    msg.innerText = "Nenhum empréstimo encontrado com esse título.";
    return;
  }

  emprestimos.splice(indexEmp, 1);
  livro.disponivel = true;
  msg.innerText = `Livro '${livro.titulo}' devolvido com sucesso!`;

  atualizarLista();
  atualizarEmprestimos();
  document.getElementById("tituloDevolucao").value = "";
}
