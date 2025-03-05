import axios from 'axios';
import type { AxiosResponse } from 'axios';

const API_URL = 'http://127.0.0.1:8000/';

interface LoginResponse {
  token: string;
  username: string;
}

interface RegisterResponse {
  message: string;
  token: string;
}

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const login = async (username: string, password: string): Promise<LoginResponse> => {
  try {
    const response: AxiosResponse<LoginResponse> = await api.post('login/', { username, password });
    return response.data;
  } catch (error) {
    console.error('Login error', error);
    throw error;
  }
};

export const register = async (username: string, password: string, email: string): Promise<RegisterResponse> => {
  try {
    const response: AxiosResponse<RegisterResponse> = await api.post('register/', { username, password, email });
    return response.data;
  } catch (error) {
    console.error('Register error', error);
    throw error;
  }
};

export const getToken = (): string | null => {
  return localStorage.getItem('token');
};

export const setToken = (token: string): void => {
  localStorage.setItem('token', token);
};

export const removeToken = (): void => {
  localStorage.removeItem('token');
};

export const setUsername = (username: string): void => {
  localStorage.setItem('username', username);
};

export const getUsername = (): string | null => {
  return localStorage.getItem('username');
};

export const removeUsername = (): void => {
  localStorage.removeItem('username');
};
