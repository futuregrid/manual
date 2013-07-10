.. actdiag::
   :desctable:


   actdiag {

      default_fontsize=14;
      node_width=300;

      A -> B -> C;
      B -> D -> E;
      D -> F;

      A [label = "1. Get Portal Account", 
         description = "Apply for a portal account at https://portal.futuregrid.org/user/register",
         color="lightgrey", shape = roundedbox];

      B [label = "Checks Identity",  width=200,
         description = "Administrator checks the data submitted."];

      C [label = "Spammer",  width=200,
         description = "Spammers will be deleted without notification."];

      D [label = "2. Wait for e-mail", 
         description = "Wait for the e-mail that approves your portal
         account. If you have not heard from us within 2 buisiness days
         use the help form on the portal to contact us.",
         color="lightgreen"];

      E [label = "3a. Create Project", width=200,
         description = "Create a new Project.", 
         color="lightgrey", shape = roundedbox];

      F [label = "3b. Join Project", width=200,
         description = "Join an existing Project.",
         color="lightgrey", shape = roundedbox];
      
      lane "User" {
         color="lightgreen";
         A;  D; E; F; 
      }
      lane "FG Administrator" {
         color="#FFFF99";
         B;
      }
      lane "Trash" {
         color="#FF3300";
         C;
      }
   }


