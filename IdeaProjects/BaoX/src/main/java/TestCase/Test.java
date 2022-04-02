package TestCase;

import Opreate.BaiduSearch;
import org.testng.annotations;

public class Test {
    BaiduSearch testSearch = new BaiduSearch();


    //测试搜索Hello,world!
    @org.testng.annotations.Test
    public void searchHelloWorld() {
        testSearch.search("Hello,world!");
    }

    @org.testng.annotations.Test
    //测试输入随机字符
    public void searchCode() {
        testSearch.search("Q￥#@%Y……");
    }

    @org.testng.annotations.Test
    //测试留空
    public void searchBlock() {
        testSearch.search("");
    }
}
