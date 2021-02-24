package com.example.monoback;

import java.util.ArrayList;
import java.util.List;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.CrossOrigin;

@RestController 
@RequestMapping("/")
@CrossOrigin
public class MonoBackController {
    
    //初期画面
    @RequestMapping("/index")
	@ResponseBody
    public List<MonoBackEntity> index() {
        return jsonData("");
    }

    //詳細画面
    @RequestMapping("/detail/**")
	@ResponseBody
	public List<MonoBackEntity> buyItem(@RequestParam("id") String id) {
        return jsonData(id);
        
    }
    
    //JSONデータ生成
    public List<MonoBackEntity> jsonData(String id) {
        List<MonoBackEntity> list = new ArrayList<>();

        if(id.equals("001") || id.equals("")){
            MonoBackEntity params1 = new MonoBackEntity();
            params1.setId("001");
            params1.setName("Tanaka");
            list.add(params1);
        }
        if(id.equals("002") || id.equals("")){
            MonoBackEntity params2 = new MonoBackEntity();
            params2.setId("002");
            params2.setName("Tamura");
            list.add(params2);
        }
        if(id.equals("003") || id.equals("")){
            MonoBackEntity params3 = new MonoBackEntity();
            params3.setId("003");
            params3.setName("Nakata");
            list.add(params3);
        }
        
        return list;
    }

}

