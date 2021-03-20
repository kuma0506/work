package com.photo.com.photo;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;

@RestController
public class PhotoController {

    @RequestMapping("/UsersRegistration")
    //ユーザー登録
    public void UsersRegistration() { 
        PhotoService.UsersRegistration();
    }
}
