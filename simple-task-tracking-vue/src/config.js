const server_domain = process.env.NODE_ENV === 'development' ? "http://localhost:5000" : "";

export const APIS = Object.freeze({
    LOGIN: server_domain + "/api/login",
    LOGOUT: server_domain + "/api/logout"
});
