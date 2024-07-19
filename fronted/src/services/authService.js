import axios from "axios"

const URL_API = "http://localhost:8000/api/"

export const login = (email, password) => {
    return axios.post(URL_API + 'token/', {
        email: email,
        password: password
    }).then(response => {
        if ( response.data.acces ) {
            localStorage.setItem('user', JSON.stringfy(response.data));
        }
        return response.data
    })
}

export const logout = () => {
    localStorage.removeItem('user')
}

export const getCurrentUser = () => {
    return JSON.parse(localStorage.getItem('user'));
};