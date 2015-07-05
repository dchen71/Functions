/*
Algorithm: MagazineView -
Sets up Applet and GUI
Makes calls to follow out its intended features
*/


import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;

public class MagazineView extends Applet implements ActionListener
{
	   MagazineList rack = new MagazineList();
	   Button remove;
	   Button removeAll;
	   TextField textInput;
	   TextField delete;
	   TextArea central;

//Sets up and draws the applet including all the positioning
	   public void init()
	   {
	      setLayout (new BorderLayout());
	      remove = new Button("Remove");
	      removeAll = new Button("Remove All");
	      textInput = new TextField("Enter Magazine", Label.CENTER);
	      delete = new TextField("Delete Magazine", Label.LEFT);
	      central = new TextArea();

	      add (textInput, "North");
	      add (central, "Center");

	      Panel s = new Panel();
	      add (s, "South");
	      s.add (delete);
	      s.add (remove);
	      s.add (removeAll);

	      remove.addActionListener(this);
	      removeAll.addActionListener(this);
	      textInput.addActionListener(this);
	   }

//Figures out what to do based on actions
	public void actionPerformed(ActionEvent e)
	{
//Does a head insert with the magazine
        if (e.getSource() == textInput)
        {
            String Input = textInput.getText();
            rack.insert (new Magazine(Input));
            central.setText(rack.toString());
            textInput.setText("");
            repaint();
        }
//Deletes a magazine from the list
        else if (e.getSource() == remove)
        {
            String removed = delete.getText();
            rack.delete(new Magazine(removed));
            central.setText(rack.toString());
            delete.setText("");
            repaint();
        }
//Calls deleteAll method
        else if (e.getSource() == removeAll)
        {
		        rack.deleteAll();
		        central.setText(rack.toString());
                textInput.setText("Enter Magazine");
                delete.setText("Delete Magazine");
	        	repaint();
        }
	}
}


