import axios from 'axios';

const apiClient = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// 添加请求拦截器，用于在每个请求头中附加Token
apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});


export const login = (credentials) => {
  const params = new URLSearchParams();
  params.append('username', credentials.username);
  params.append('password', credentials.password);

  return apiClient.post('/auth/login', params, {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  });
};

export const verifyToken = () => {
  return apiClient.get('/auth/me');
};
