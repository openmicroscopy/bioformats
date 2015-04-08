/*
 * #%L
 * OME Bio-Formats package for reading and converting biological file formats.
 * %%
 * Copyright (C) 2005 - 2015 Open Microscopy Environment:
 *   - Board of Regents of the University of Wisconsin-Madison
 *   - Glencoe Software, Inc.
 *   - University of Dundee
 * %%
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as
 * published by the Free Software Foundation, either version 2 of the 
 * License, or (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public 
 * License along with this program.  If not, see
 * <http://www.gnu.org/licenses/gpl-2.0.html>.
 * #L%
 */

package loci.formats.in;

import java.util.Hashtable;
import java.util.Vector;

import loci.common.xml.BaseHandler;

import ome.units.UNITS;
import ome.units.quantity.Length;

import org.xml.sax.Attributes;

/**
 * MetamorphTiffReader is the file format reader for TIFF files produced by
 * Metamorph software version 7.5 and above.
 *
 * @author Melissa Linkert melissa at glencoesoftware.com
 * @author Thomas Caswell tcaswell at uchicago.edu
 */
public class MetamorphHandler extends BaseHandler {

  // -- Fields --

  private Hashtable metadata;

  private Vector<String> timestamps;
  private String imageName;
  private String date;
  private Vector<Integer> wavelengths;
  private Vector<Double> zPositions;
  private double pixelSizeX, pixelSizeY;
  private double temperature;
  private String binning;
  private double readOutRate, zoom;
  private Length positionX, positionY;
  private Vector<Double> exposures;
  private String channelName;
  private String stageLabel;
  private Double gain;

  private String[] mDesciptionKeyList = {
    "Plate Screen", "Acquired from Photometrics", "Barcode:",
    "Experiment base name:", "Experiment set:", "Exposure:",
    "Binning:", "Region:", "Subtract:", "Shading:", "Digitizer:",
    "Gain:", "Camera Shutter:", "Clear Count:", "Clear Mode:",
    "Frames to Average:", "Trigger Mode:", "Temperature:"
  };


  // -- Constructor --

  public MetamorphHandler() {
    this(null);
  }

  public MetamorphHandler(Hashtable metadata) {
    super();
    this.metadata = metadata;
    timestamps = new Vector<String>();
    wavelengths = new Vector<Integer>();
    zPositions = new Vector<Double>();
    exposures = new Vector<Double>();
  }

  // -- MetamorphHandler API methods --

  public Double getGain() { return gain; }

  public String getChannelName() { return channelName; }

  public String getStageLabel() { return stageLabel; }

  public Vector<String> getTimestamps() { return timestamps; }

  public Vector<Integer> getWavelengths() { return wavelengths; }

  public Vector<Double> getZPositions() { return zPositions; }

  public String getDate() { return date; }

  public String getImageName() { return imageName; }

  public double getPixelSizeX() { return pixelSizeX; }

  public double getPixelSizeY() { return pixelSizeY; }

  public double getTemperature() { return temperature; }

  public String getBinning() { return binning; }

  public double getReadOutRate() { return readOutRate; }

  public double getZoom() { return zoom; }

  public Length getStagePositionX() { return positionX; }

  public Length getStagePositionY() { return positionY; }

  public Vector<Double> getExposures() { return exposures; }

  public void parseTextDescription(String desc)
  {
    if (desc == null)
      return;

    if (metadata != null) metadata.remove("Comment");

    String k = null, v = null;

    String delim = " #13; #10;";
    if (desc.indexOf(delim) < 0) {
      delim = "&#13;&#10;";
    }
    if (desc.indexOf(delim) < 0) {
      delim = "\n";
    }

    if (desc.indexOf(delim) != -1) {
      String vDescription = null;

      int currentIndex = 0;
      while (currentIndex != -1) {
        int nextIndex = desc.indexOf(delim, currentIndex);

        String line = null;
        if (nextIndex == -1) {
          line = desc.substring(currentIndex, desc.length());
        }
        else {
          line = desc.substring(currentIndex, nextIndex);
        }
        currentIndex = nextIndex;
        if (currentIndex != -1)
          currentIndex += delim.length();

        if (line.isEmpty()) {
          continue;
        }

        // We use a dictionary to identify the standard MetaMorph keys:
        boolean vLineIsMetaMorphStandard = false;
        for (String vDescriptionKey : mDesciptionKeyList) {
          if (line.startsWith(vDescriptionKey)) {
            vLineIsMetaMorphStandard = true;
            break;
          }
        }
        if (vLineIsMetaMorphStandard) {
          // The majority of tags can be split at the colon:
          int colon = line.indexOf(":");
          if (colon != -1) {
            k = line.substring(0, colon).trim();
            v = line.substring(colon + 1).trim();
            if (metadata != null) metadata.put(k, v);
            checkKey(k, v);
          } else {
            // There was no colon, so the key is a full line:
            k = line.trim();
            v = line.trim();
            if (metadata != null) metadata.put(k, v);
            checkKey(k, v);
          }
        } else {
          // This is NOT a standard tag in the description field, so it
	      // must be a multi-line description from the user (i.e. from
	      // the MetaXpress free-text "Description" field in the screening
	      // application).
          if (vDescription == null) {
            vDescription = line;
          } else {
            vDescription = vDescription + "\n" + line;
          }
        }
      }
      if (metadata != null && vDescription != null) metadata.put("Description", vDescription);
    }
    else {
      int colon = desc.indexOf(":");
      while (colon != -1) {
        k = desc.substring(0, colon);
        int space = desc.lastIndexOf(" ", desc.indexOf(":", colon + 1));
        if (space == -1) space = desc.length();
        v = desc.substring(colon + 1, space).trim();
        if (metadata != null) metadata.put(k, v);
        desc = desc.substring(space).trim();
        colon = desc.indexOf(":");
        checkKey(k, v);
      }
    }
  }

  // -- DefaultHandler API methods --


  @Override
  public void startElement(String uri, String localName, String qName,
    Attributes attributes)
  {
    String id = attributes.getValue("id");
    String value = attributes.getValue("value");
    if (id != null && value != null) {
      if (id.equals("Description")) {
        parseTextDescription(value);
      }
      else {
        if (metadata != null) metadata.put(id, value);
        checkKey(id, value);
      }
    }
  }

  // -- Helper methods --

  /** Check if the value needs to be saved. */
  private void checkKey(String key, String value) {
    if (key.equals("Temperature")) {
      temperature = Double.parseDouble(value);
    }
    else if (key.equals("spatial-calibration-x")) {
      pixelSizeX = Double.parseDouble(value);
    }
    else if (key.equals("spatial-calibration-y")) {
      pixelSizeY = Double.parseDouble(value);
    }
    else if (key.equals("z-position")) {
      zPositions.add(new Double(value));
    }
    else if (key.equals("wavelength")) {
      wavelengths.add(new Integer(value));
    }
    else if (key.equals("acquisition-time-local")) {
      date = value;
      timestamps.add(date);
    }
    else if (key.equals("image-name")) imageName = value;
    else if (key.equals("Binning")) {
      binning = value;
    }
    else if (key.equals("Readout Frequency")) {
      readOutRate = Double.parseDouble(value);
    }
    else if (key.equals("zoom-percent")) {
      zoom = Double.parseDouble(value);
    }
    else if (key.equals("stage-position-x")) {
      final Double number = Double.valueOf(value);
      positionX = new Length(number, UNITS.REFERENCEFRAME);
      if (metadata != null) {
        metadata.put("X position for position #1", positionX);
      }
    }
    else if (key.equals("stage-position-y")) {
      final Double number = Double.valueOf(value);
      positionY = new Length(number, UNITS.REFERENCEFRAME);
      if (metadata != null) {
        metadata.put("Y position for position #1", positionY);
      }
    }
    else if (key.equals("Speed")) {
      int space = value.indexOf(" ");
      if (space > 0) {
        value = value.substring(0, space);
      }
      try {
        readOutRate = Double.parseDouble(value.trim());
      }
      catch (NumberFormatException e) { }
    }
    else if (key.equals("Exposure")) {
      if (value.indexOf(" ") != -1) {
        value = value.substring(0, value.indexOf(" "));
      }
      // exposure times are stored in milliseconds, we want them in seconds
      try {
        exposures.add(new Double(Double.parseDouble(value) / 1000));
      }
      catch (NumberFormatException e) { }
    }
    else if (key.equals("_IllumSetting_")) {
      channelName = value;
    }
    else if (key.equals("stage-label")) {
      stageLabel = value;
    }
    else if (key.endsWith("Gain") && gain == null) {
      try {
        gain = new Double(value.replaceAll("[xX]", ""));
      }
      catch (NumberFormatException e) { }
    }
  }

}
