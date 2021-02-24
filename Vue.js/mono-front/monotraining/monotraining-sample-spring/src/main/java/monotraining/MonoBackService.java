package monotraining;

import java.sql.Date;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import javax.persistence.PrePersist;
import javax.transaction.Transactional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.ui.Model;

import io.sitoolkit.dba.domain.users.UsersEntity;

@Transactional
@Service
public class MonoBackService {
    
	@Autowired
    MonoBackRepository monoBackRepository;

    //初期画面
    public List<UsersEntity> index() {
        List<UsersEntity> list = monoBackRepository.findAllByOrderById();
        return list;
    }

    //詳細画面
    public Optional<UsersEntity> detail(String id) {
        Optional<UsersEntity> list = monoBackRepository.findById(id);
        return list;
    }

    //登録画面
    public void insert(String id, String name){
        UsersEntity newEntity = new UsersEntity(id, name);
        monoBackRepository.save(newEntity);
    }

    //更新処理
    public void update(String id, String name) {
        UsersEntity newEntity = new UsersEntity(id, name);
        monoBackRepository.deleteById(id);
        monoBackRepository.save(newEntity);
    }

    // 削除処理
    public void delete(String id) {
        monoBackRepository.deleteById(id);
    }

    public String getId() {
        //すべての登録データ取得
        List<UsersEntity> list = monoBackRepository.findAllByOrderById();
        //最後に登録したデータのid取得
        String arg = list.get(list.size()-1).getId();
        //idを数値化して+1する
        int arg1 = Integer.parseInt(arg) + 1;
        //idを再び文字列可し、先頭に"00"する
        String arg2 = ("00"+Integer.toString(arg1));
        //右から3桁を切り出し、idとする
        String id = arg2.substring(arg2.length()-3);
        System.out.println("--------------");
        System.out.println(arg);
        System.out.println(arg1);
        System.out.println(arg2);
        System.out.println(id);
        System.out.println("--------------");
        return id;
    }
}
