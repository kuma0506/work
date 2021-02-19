package a.b.c.interfaces.repository;

import org.springframework.stereotype.Repository;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.RowMapper;
import a.b.c.interfaces.entity.OrderPdtListEntity;

@Repository
public class OrderRepository {
    @Autowired
    JdbcTemplate jdbcTemplate;
    
    //productテーブル情報取得
    public List<OrderPdtListEntity> productList() {

        String sql = "SELECT * FROM product";
        RowMapper<OrderPdtListEntity> rowMapper = new BeanPropertyRowMapper<OrderPdtListEntity>(OrderPdtListEntity.class);

		return jdbcTemplate.query(sql, rowMapper);
    } 

    //orderテーブルのシーケンスオブジェクトを取得
    public String orderNumber() {

        //String sql = "SELECT LAST_INSERT_ID() kensu FROM `order` LIMIT 1";
        //String num = jdbcTemplate.queryForList(sql).toString();
        //System.out.println(num);
    
        return "00001";
    }
}