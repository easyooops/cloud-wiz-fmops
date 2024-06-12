import axios from 'axios';

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
  const get = async (url, header) => {
    return await useFetch(`${API_ENDPOINT}${url}`, {
      method: 'GET',
      headers: header == null ? { 'Content-Type': 'application/json' } : header
    });
  };

  const post = async (url, body, header) => {
    return await useFetch(`${API_ENDPOINT}${url}`, {
      method: 'POST',
      headers: header == null ? { 'Content-Type': 'application/json' } : header,
      body: JSON.stringify(body)
    });
  };

  const put = async (url, body, header) => {
    return await useFetch(`${API_ENDPOINT}${url}`, {
      method: 'PUT',
      headers: header == null ? { 'Content-Type': 'application/json' } : header,
      body: JSON.stringify(body)
    });
  };

  const del = async (url, header) => {
    return await useFetch(`${API_ENDPOINT}${url}`, {
      method: 'DELETE',
      headers: header == null ? { 'Content-Type': 'application/json' } : header
    });
  };

  return { get, post, put, del };
};

export default restApi;
