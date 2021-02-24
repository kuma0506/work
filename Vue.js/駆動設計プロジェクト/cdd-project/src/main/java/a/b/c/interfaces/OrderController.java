package a.b.c.interfaces;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import a.b.c.interfaces.service.*;
import a.b.c.interfaces.repository.*;
import org.springframework.ui.Model;
import java.util.List;
import a.b.c.interfaces.entity.OrderPdtListEntity;

@Controller
public class OrderController {
    
    @Autowired
    OrderService orderService;
    
    @Autowired
    OrderRepository orderRepository;

    @RequestMapping(value="/")
    public String index(Model model){
        //productテーブルからリストを取得する
        List<OrderPdtListEntity> productlist = orderRepository.productList();
        model.addAttribute("productlist", productlist);
        
        return "./index.html";
    }
     
    @RequestMapping(value="/shop")
    public String shop(Model model){
        System.out.println("done");

        //オーダー番号取得(yyMMddHHmm00000)
        String orderNumber = orderService.getOrderNumber();

        model.addAttribute("orderNumber", orderNumber);
        return "./shop.html";
    }

}
