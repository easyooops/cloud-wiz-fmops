import axios from 'axios';
import { useAuthStore } from '@/store/auth';

const API_ENDPOINT = import.meta.env.VITE_API_ENDPOINT+'/api/v1';

const useFetch = async (url, options) => {
  try {
    const response = await axios({
      url,
      method: options.method,
      headers: options.headers,
      data: options.body
    });
    return response;
  } catch (error) {
    throw error;
  }
};

const restApi = () => {

  const authStore = useAuthStore();

  const get = async (url) => {
    return await useFetch(`${API_ENDPOINT}${url}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    });
  };

  const post = async (url, body) => {
    return await useFetch(`${API_ENDPOINT}${url}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify(body)
    });
  };

  const put = async (url, body) => {
    return await useFetch(`${API_ENDPOINT}${url}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify(body)
    });
  };

  const del = async (url) => {
    return await useFetch(`${API_ENDPOINT}${url}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
    });
  };

  return { get, post, put, del };
};

export default restApi;
