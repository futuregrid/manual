
.. actdiag::
   :desctable:

   actdiag {

      default_fontsize=14;
      node_width=300;

      create -> review -> wait -> approved;

      approved -> members;
      approved -> results -> resultreview -> renewal;

      create [label = "3a. Create new Project", 
         description = "Fill out the project form at https://portal.futuregrid.org/node/add/fg-projects",
         color="lightgrey", shape = roundedbox];

      review [label = "Review", width=200,
              description = "Committee reviews the project and corresponds with project lead to improve"];

      wait [label = "3a.1. Wait for e-mail", description = "Wait for an e-mail
         that you have an account", 
         color="lightgrey", shape = roundedbox];


      approved [label = "3a.2. Project Approved", 
         description = "The project has been approved.",
         color = "lightgreen"];

      members [label = "3a.3.i. Members add, del., alumni", 
          description = "manage the project members"]

      results [label = "3a.3.ii. Report Results", 
          description = "Make project member Alumni"]

      resultreview [label = "Review Results", width=200,
          description = "Committee receives results for review"]

      renewal [label = "4. Renewal", 
          description = "Renewal of the project",
	  color="lightgrey", shape = roundedbox];

      lane "FG Project Lead" {
         color="lightgreen";
         create; wait; approved; members; renewal;
      }
      lane "Committee" {
         color="#FFFF99";
         review; resultreview
      }
      
   }
