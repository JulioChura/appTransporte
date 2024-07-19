import axios from 'axios';

// Configura la URL de tu API Django
const API_URL = 'http://localhost:8000/api/'; 

// Función para login
export const login = (email, password) => {
    return axios.post(`${API_URL}clientes/login/`, {
        email,
        password
    });
};

// Almacenar token en localStorage
export const setToken = (token) => {
    localStorage.setItem('token', token);
};

// Obtener token de localStorage
export const getToken = () => {
    return localStorage.getItem('token');
};

// Eliminar token de localStorage
export const logout = () => {
    localStorage.removeItem('token');
};
