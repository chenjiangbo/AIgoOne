import axios from 'axios';

const apiClient = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export const getDevices = (params) => {
  return apiClient.get('/devices/', { params });
};

export const addDevice = (deviceData) => {
  return apiClient.post('/devices/', deviceData);
};

export const updateDevice = (deviceId, deviceData) => {
  return apiClient.put(`/devices/${deviceId}`, deviceData);
};

export const deleteDevice = (deviceId) => {
  return apiClient.delete(`/devices/${deviceId}`);
};

export const syncDevice = (deviceId) => {
  return apiClient.post(`/devices/${deviceId}/sync`);
};

export const batchSyncDevices = (deviceIds) => {
  return apiClient.post('/devices/batch-sync', { device_ids: deviceIds });
};

export const getDeviceDetails = (deviceId) => {
  return apiClient.get(`/devices/${deviceId}`);
};

export const batchImportDevices = (devicesData) => {
  return apiClient.post('/devices/batch-import', devicesData);
};

export const batchDeleteDevices = (deviceIds) => {
  return apiClient.delete('/devices/batch-delete', {
    data: { device_ids: deviceIds }
  });
};
