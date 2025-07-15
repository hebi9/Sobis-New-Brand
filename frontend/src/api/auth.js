import axios from "axios";

export async function loginUser(credentials) {
  const response = await axios.post('http://localhost:8000/api/token/', credentials);
  return response.data;
}
