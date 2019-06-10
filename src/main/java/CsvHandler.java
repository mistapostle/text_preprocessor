import com.csvreader.CsvReader;
import com.csvreader.CsvWriter;

import java.io.IOException;

public class CsvHandler {
    public static void main(String[] args) throws IOException {
        CsvWriter csvWriter = new CsvWriter("test.csv");
        csvWriter.writeRecord(new String[]{"content" , "label" } );
        csvWriter.write("<html abc \"ok  \" > what else \n what is this  </html> ");
        csvWriter.write("b is b ");
        csvWriter.endRecord();
        csvWriter.flush();
        csvWriter.close();

        CsvReader csvReader = new CsvReader("test.csv");
        csvReader.readHeaders();
        while (csvReader.readRecord()){
            // 读一整行
            System.out.println(csvReader.getRawRecord());
            // 读这行的某一列
            System.out.println("content:" +  csvReader.get("content"));
            System.out.println("label:" + csvReader.get("label"));
        }
    }
}
