
.. actdiag::
   :desctable:

   actdiag {

      default_fontsize=14;
      node_width=300;

      F -> G -> H;
      G -> I -> J -> M;
      M -> K -> L; 

      F [label = "3b. Join Project?", 
         description = "Join an existing Project.",
         color="lightgrey", shape = roundedbox];

      G [label = "Get Permission", width=200,
         description = "Get permission from the project lead to join
         the project."];

      H [label = "Delete Join Request",  width=200,
         description = "Project leads will carefully evaluate if the
         person requesting to join is eligible. If not join requests will be
         deleted without notification requires to those that want to join."];


      I [label = "3b.1. Join Approved", 
         description = "The project lead has approved that you join
         the project. Go to the project page and press the join button/link.",
         color = "lightgreen"];

      J [label = "Project Active",  width=200,
         description = "Checks if the project is active
         the project."];

      M [label = "3b.2. SSH key uploaded?", description = "You must have
         uploaded your ssh key to use FutureGrid resources",
         color = "lightgreen"];

      K [label = "Generate Accounts",  width=200,
         description = "Generate accounts to resources"]

      L [label = "3b.3. Wait for e-mail", description = "Wait for an e-mail
         that you have an account", 
         color="lightgrey", shape = roundedbox];
      
      lane "User" {
         color="lightgreen";
         F; I; M; L;
      }
      lane "FG Project Lead" {
         color="#FFFF99";
         G;
      }
      lane "System" {
         color="#FFFF99";
         J; K;
      }
      lane "Trash" {
         color="#FF3300";
         H;
      }
   }
