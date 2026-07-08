import { useEffect, useState } from "react";

function App() {

  const [msg, setMsg] = useState("");

  useEffect(() => {

    fetch("http://localhost:8000/")
      .then(res => res.json())
      .then(data => setMsg(data.mensagem));

  }, []);

  return (
    <div>
      <h1>Meu Site</h1>

      <h2>{msg}</h2>

    </div>
  );
}

export default App;