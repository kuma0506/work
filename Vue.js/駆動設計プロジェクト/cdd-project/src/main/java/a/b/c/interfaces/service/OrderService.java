package a.b.c.interfaces.service;

import org.springframework.beans.factory.annotation.Autowired;
import a.b.c.interfaces.repository.*;
import org.springframework.stereotype.Service;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import a.b.c.interfaces.entity.*;

@Service
public class OrderService {

    @Autowired
    OrderRepository orderRepository;

    public String order(OrderEntity order) {
        order.setOrderNumber("00001");
        return order.getOrderNumber();
    }

    public String getOrderNumber() {
        //現在日時取得
        Date date = new Date();
        DateFormat dateFormat1 = new SimpleDateFormat("yyMMddHHmm");

        //オーダー番号取得
        String orderNumber = orderRepository.orderNumber();

        //現在日時(yyMMddHHmm)+オーダー番号(00000)
        return dateFormat1.format(date) + orderNumber;
    }

  }