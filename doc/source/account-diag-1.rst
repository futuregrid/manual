
.. actdiag::
   :desctable:

   actdiag {

      F -> G -> H;
      G -> I -> J -> M;
      M -> K -> L; 

      F [label = "3b. Join Project?", 
         description = "Join an existing Project.",
         color="lightgrey", shape = roundedbox];

      G [label = "Get Permission", 
         description = "Get permission from the project lead to join
         the project."];

      H [label = "Delete Join Request", 
         description = "Project leads will carefully evaluate if the
         person requesting to join is elidgeble. If not join requests will be
         deleted without notification requires to those that want to join."];


      I [label = "3b.1. Join Approved", 
         description = "The project lead has approved that you join
         the project. Go to the project page and press the join button/link.",
         color = "lightgreen"];

      J [label = "Project Active", 
         description = "Checks if the project is actve
         the project."];

      M [label = "3b.2. SSH key\n uploaded?", description = "You must have
         uploaded your ssh key to use Futuregrid resources",
         color = "lightgreen"];

      K [label = "Generate Accounts", description = "Generate accounts
         to resources"]

      L [label = "3b.3. Wait for\n e-mail", description = "Wait for an e-mail
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
