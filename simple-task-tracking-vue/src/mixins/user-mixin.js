// Note: Mixin is a normal exported object when it is defined.
//       As long as you export the object, you can import it in other files
//       the benefit of use it as a mixin in another component is you have access to the component's vue instance, i.e., "this".

import {API, RESOURCES} from "../config";
import Axios from "axios";

export const UserMixin = {
    methods: {
        updateUserSession(userInfoObject) {
            this.$session.loggedIn = true;
            this.$session.displayName = userInfoObject.displayName;
            this.$session.userName = userInfoObject.userName;
            this.$session.email = userInfoObject.email;
            this.$session.avatarUrl = userInfoObject.avatarUrl ? userInfoObject.avatarUrl : RESOURCES.DEFAULT_USER_AVATAR;
            this.$session.gender = userInfoObject.gender;
            this.$session.role = userInfoObject.role;
            this.$session.department = userInfoObject.department;
        },

        resetUserSession() {
            this.$session.loggedIn = false;
            this.$session.displayName = null;
            this.$session.userName = null;
            this.$session.email = null;
            this.$session.avatarUrl = null;
            this.$session.gender = null;
            this.$session.role = null;
            this.$session.department = null;
        },

        checkLoggedIn() {
            if (this.$session.loggedIn == null) {
                // Only make a call when loggedIn status is unknown.
                Axios.get(API.USER_INFO, {withCredentials: true})
                    .then(response => {
                        if (response.data.success) {
                            this.updateUserSession(response.data.payload);
                            this.$forceUpdate();
                        } else {
                            this.resetUserSession();
                        }
                    })
                    .catch(err => {
                        console.log(err);
                        this.resetUserSession();
                    });
            }
        },

        signOut() {
            if (this.$session.loggedIn) {
                Axios.get(API.LOGOUT, {withCredentials: true})
                    .then(() => {
                        this.resetUserSession();
                        location.reload();
                    })
                    .catch(err => {
                        console.log(err);
                        this.resetUserSession();
                        location.reload();
                    });
            }
            // TODO: clear cookies
        }
    }
}

