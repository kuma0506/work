package monotraining;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import io.sitoolkit.dba.domain.users.UsersEntity;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.CrossOrigin;

@RestController
@CrossOrigin
@Transactional

public class MonoBackController {

    // 初期画面
    @Autowired
    MonoBackRepository monoBackRepository;

    @Autowired
    MonoBackService monoBackService;

    @RequestMapping("/")
    //初期画面
    public List<UsersEntity> index(Model model) {
        System.out.println("index");
        List<UsersEntity> list = monoBackService.index();
        model.addAttribute("list", list);
        return list;
    }

    //詳細画面
    @RequestMapping("/detail/**")
	@ResponseBody
	public Optional<UsersEntity> detail(@RequestParam("id") String id) {
        Optional<UsersEntity> list = monoBackService.detail(id);
        System.out.println("detail");
        return list;
    }
        
    // 登録画面
    @RequestMapping("/insert/**")
    @ResponseBody
    public void insert(@RequestParam("name") String name) {
        System.out.println("insert");
        //id取得（xxx）
        String id = monoBackService.getId();
        System.out.println("1:"+id);
        monoBackService.insert(id,name);
        
    }

    // 更新処理
    @RequestMapping("/update/**")
    @ResponseBody
    public void update(@RequestParam("id") String id, @RequestParam("name") String name) {
        System.out.println("update");
        monoBackService.update(id,name);

    }

    // 削除処理
    @RequestMapping("/delete/**")
    @ResponseBody
    public void delete(@RequestParam("id") String id) {
        System.out.println("delete");
        monoBackService.delete(id);
        
    }
    
}

