const server_domain = process.env.NODE_ENV === 'development' ? "http://localhost:5000" : "";

export const API = Object.freeze({
    LOGIN: server_domain + "/api/login",
    LOGOUT: server_domain + "/api/logout",
    USER_INFO: server_domain + "/api/user_info",
});

export const RESOURCES = Object.freeze({
    DEFAULT_USER_AVATAR: "./assets/default_user.png",
})
