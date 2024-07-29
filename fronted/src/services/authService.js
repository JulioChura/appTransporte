import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

export const login = async (email, password) => {
    console.log('Attempting login with:', email);
    try {
        const response = await axios.post(`${API_URL}login/`, { email, password });
        console.log('Login response:', response.data);
        if (response.data.token) {
            localStorage.setItem('user', JSON.stringify(response.data));
            console.log('User data stored in localStorage');
        }
        return response.data;
    } catch (error) {
        console.error('Login error:', error.response ? error.response.data : error.message);
        throw error;
    }
};

export const logout = () => {
    console.log('Logging out user');
    localStorage.removeItem('user');
};

export const register = async (userData) => {
    console.log('Attempting to register user:', userData);
    try {
        const response = await axios.post(`${API_URL}register/`, userData);
        console.log('Registration response:', response.data);
        return response.data;
    } catch (error) {
        console.error('Registration error:', error.response ? error.response.data : error.message);
        throw error;
    }
};

export const getCurrentUser = () => {
    const user = JSON.parse(localStorage.getItem('user'));
    console.log('Current user:', user);
    return user;
};

axios.interceptors.request.use(
    (config) => {
        const user = getCurrentUser();
        if (user && user.token) {
            console.log('Adding token to request');
            config.headers['Authorization'] = 'Token ' + user.token;
        }
        return config;
    },
    (error) => {
        console.error('Request interceptor error:', error);
        return Promise.reject(error);
    }
);

