import axios from "axios";

const API_BASE_URL =
  window.location.hostname === "localhost"
    ? "http://localhost:8000"
    : "https://hebi.pythonanywhere.com";


export async function loginUser(credentials) {
  const response = await axios.post(`${API_BASE_URL}/api/token/`, credentials);
  return response.data;
}
