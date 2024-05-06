import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
const Login = () => {
 const [username, setUsername] = useState('');
 const [password, setPassword] = useState('');
 const [msg, setMsg] = useState('');
 const [error, setError] = useState('');
 const handleLogin = async (e) => {
 e.preventDefault();
 try {
 const response = await fetch('http://localhost:8000/PastelDeNata/login/', {
 method: 'POST',
 headers: {
 'Content-Type': 'application/json',
 },
 body: JSON.stringify({ username, password }),
 });
 const data = await response.json();
 if (response.ok) {
 // Fez Login com sucesso
 // Guarda o token para invocações futuras durante a sessão
 localStorage.setItem('token', data.token);
 // Imprime msg de sucesso ou redireciona
 setMsg('Viva, fez login !');
 } else {
 setError(data.error || 'Algo errado');
 }
 } catch (error) {
 console.error('Login falhou:', error);
 setError('Algo errado');
 }
 };
 return (
 <div>
 <h2>Login</h2>
 {error && <p>{error}</p>}
 {<p>{msg}</p>}
 <form onSubmit={handleLogin}>
 <input
 type="text"
 placeholder="Username"
 value={username}
 onChange={(e) => setUsername(e.target.value)}
 />
 <input
 type="password"
 placeholder="Password"
 value={password}
 onChange={(e) => setPassword(e.target.value)}
 />
 <button type="submit">Login</button>
 </form>
 </div>
 );
};
export default Login;
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Login />);
