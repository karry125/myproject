package TestCase;

import Opreate.CreateOpreate;
import org.testng.annotations.Test;

import java.io.IOException;

public class TestCreate {

    CreateOpreate op=new CreateOpreate();
    @Test
    public void Testnew() throws IOException, InterruptedException {
        op.clickNew();
    }

    public void Testout() throws InterruptedException {
        op.clickOut();
    }
}
