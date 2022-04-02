package TestCase;

import Opreate.CreatePuOpreate;
import org.testng.annotations.Test;

public class TestCreatePu {
    CreatePuOpreate pu=new CreatePuOpreate();
  @Test
    public void TestPu(){

        pu.create();
    }
}
