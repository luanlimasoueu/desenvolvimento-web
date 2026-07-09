import { useEffect, useState } from "react";

function App() {
  const [msg, setMsg] = useState("Carregando...");

  useEffect(() => {
    console.log("Chamando API...");

    fetch("http://localhost:8000/")
      .then((res) => {
        console.log("Status:", res.status);
        return res.json();
      })
      .then((data) => {
        console.log("Resposta:", data);
        setMsg(data.mensagem);
      })
      .catch((err) => {
        console.error("Erro:", err);
        setMsg("Erro ao conectar");
      });
  }, []);

  return (
    <div>
      <h1>Meu Site</h1>
      <h2>{msg}</h2>
    </div>
  );
}

export default App;