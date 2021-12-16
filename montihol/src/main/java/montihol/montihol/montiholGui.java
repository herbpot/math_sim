package montihol.montihol;

import org.bukkit.Bukkit;
import org.bukkit.Material;
import org.bukkit.entity.Player;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.ItemStack;

public class montiholGui {
    public void gui(Player p){
        Inventory inv = Bukkit.createInventory(null,18,"몬티홀");
        ItemStack item1,item2,item3;
        item1 = new ItemStack(Material.CRIMSON_DOOR);
        item2 = new ItemStack(Material.DARK_OAK_DOOR);
        item3 = new ItemStack(Material.JUNGLE_DOOR);
        //0 1. 2 3 4. 5 6 7. 8
        inv.setItem(1,item1);
        inv.setItem(4,item2);
        inv.setItem(7,item3);
        p.openInventory(inv);
    }
}
