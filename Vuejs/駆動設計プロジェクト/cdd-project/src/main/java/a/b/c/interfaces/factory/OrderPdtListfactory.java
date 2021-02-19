package a.b.c.interfaces.factory;

import java.sql.ResultSet;
import java.sql.SQLException;
import org.springframework.jdbc.core.RowMapper;
import a.b.c.interfaces.entity.*;

public class OrderPdtListfactory  implements RowMapper<OrderPdtListEntity> {
    @Override
    public OrderPdtListEntity mapRow(ResultSet rs, int rowNum) throws SQLException {

        //戻り値用のUserインスタンスを生成
        OrderPdtListEntity product = new OrderPdtListEntity();

        //ResultSetの取得結果をUserインスタンスにセット
        product.setProductCd(rs.getString("product_cd"));
        product.setProductName(rs.getString("produst_Name"));

        return product;
    }
}
