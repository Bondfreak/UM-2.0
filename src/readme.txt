App: customUser

UseCase-1: go to the Admin site
    path = "admin/"

UseCase-2: display the hope page
    name = "home"    
    path = '""' 
    view = home_screen_view
    template = "home.html"

UseCase-3: let a new user register
    name = "register"
    path = "register/"
    view = registration_view
    form = RegistrationForm
    template = "register.html"

UseCase-4: let the user logout 
    name = "logout"
    path = "logout/" 
    view = logout_view

UseCase-5: let the user login   
    name = "login"
    path = "login/"
    view = login_view
    form = CustomUserAuthenticationForm
    template = "login.html"

UseCase-6: let the user update personal data
    name = "customUserUpdateMyData"
    path = "user/"
    view = custom_user_update_my_data_view
    form = CustomUserChangeForm
    template = "custom_user_update_my_data.html"

UseCase-7: list all users with update and delete options
    name = "customUserList"
    path = "list/" 
    view = custom_user_list_view
    template = "custom_user_list.html"

UseCase-8: add a new user
    name = "customUserAdd"
    path = "add/" 
    view = custom_user_add_view
    form = RegistrationForm
    template = "user/custom_user_add.html"

UseCase-9: update another users personal data
    name = "customUserUpdate"
    path = "update/<pk>/"
    view = custom_user_update_view
    form = CustomUserChangeForm
    template = "user/custom_user_update.html"

UseCase-10: delete another user
    name = "customUserDelete"    
    path = "delete/<pk>/"
    view = custom_user_delete_view
    form = CustomUserChangeForm
    template = "user/custom_user_delete.html"

UseCase-11: show that the password was changed   
    name = "password_change_done"
    path = "password_change/done/"
    template = "password_change_done.html"

UseCase-12: change the user password    
    name = "password_change"
    path = "password_change/"
    template = "password_change.html"

UseCase-13: show that the password was reset
    name = "password_reset_done"
    path = "password_reset/done/"
    template = "password_reset_done.html"

UseCase-14: confirm the reset of password
    name = "password_reset_confirm"
    path = "reset/<uidb64>/<token>/"

UseCase-15: reset the user password  
    name = "password_reset"
    path = "password_reset/"
    template = "password_reset_form.html"

UseCase-16: display reset
    name = "password_reset_complete"
    path = "reset/done/"
    template = password_reset_complete.html
