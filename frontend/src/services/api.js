import axios from "axios";

const API = axios.create({
  baseURL: "http://13.233.130.128:8000"
})

export default API;