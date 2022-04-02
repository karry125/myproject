package Opreate;

import Action.BaiduSearchPageAction;
import Page.BaiduSearchPageElements;
import Page.ListBx;
import Opreate.Login;
import org.openqa.selenium.WebElement;

public class ListOpreate {
    //声明元素类和操作类
    ListBx list=new ListBx();
    BaiduSearchPageAction action = new BaiduSearchPageAction();

    public void clickMylist(){
        System.out.print(  list.clickleft(Login.driver).size());
        if(list.clickleft(Login.driver).size()!=0){
            System.out.print(  list.clickleft(Login.driver).size());
            action.click(list.clickleft(Login.driver).get(0));

            action.click(list.clickleft(Login.driver).get(1));
            System.out.print("a");
        }
    }
}
