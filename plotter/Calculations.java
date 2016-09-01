import java.awt.*;
import java.util.*;
import java.awt.event.*;
import javax.swing.*;
public class Calculations extends JApplet
     implements ActionListener
{
    private JTextField inputField;
    int prevx,prevy;
    String str="";
    app ob=new app();
    public void init()
    {
         
     prevx=prevy=0;
       Container contentPane = getContentPane();
        contentPane.setLayout(new BorderLayout(12,12));
        JPanel centerPanel = new JPanel();
        inputField = new JTextField(44);
        centerPanel.add(inputField);
        contentPane.add(centerPanel, BorderLayout.NORTH);
        JPanel buttonPanel = new JPanel();
        JButton uppercase = new JButton("show");
        uppercase.addActionListener(this);
        buttonPanel.add(uppercase);
        JButton clear = new JButton("clear");
        clear.addActionListener(this);
        buttonPanel.add(clear);
        contentPane.add(buttonPanel, BorderLayout.SOUTH);
       contentPane.add(ob, BorderLayout.CENTER);
       inputField.setText("Type 'help' to get help! ;-)  -Shantanu");
    }

    public String getAppletInfo()
    {
        return "Title: CALCULATER  \n" +
               "Author: SHANTANU GUPTA  \n" ;
    }
//(sin(7*x/6)+sin(5*x/6)+sin(9*x/6)+sin(3*x/6))/(cos(7*x/6)+cos(5*x/6)+cos(9*x/6)+cos(3*x/6)=tanx
    public void actionPerformed(ActionEvent evt)
    {
         String command = evt.getActionCommand();
        if("clear".equals(command))
            inputField.setText(ob.str="");
            else
            ob.str=inputField.getText().toLowerCase()+",$";  
            ob.repaint();
    }
    

	

}