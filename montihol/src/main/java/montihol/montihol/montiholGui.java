package montihol.montihol;

import org.bukkit.Bukkit;
import org.bukkit.Material;
import org.bukkit.entity.Player;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.ItemStack;

public class montiholGui {
    public void gui(Player p){
        Inventory inv = Bukkit.createInventory(null,18,"몬티홀");
        ItemStack item1,item2,item3,item4;
        item1 = new ItemStack(Material.CRIMSON_DOOR);
        item2 = new ItemStack(Material.DARK_OAK_DOOR);
        item3 = new ItemStack(Material.JUNGLE_DOOR);
        item4 = new ItemStack(Material.OAK_SIGN);

        ItemMeta meta = item4.getItemMeta();
        meta.setDisplayName("알리미");
        meta.setLore(Arrays.asList(
            "몬티혼 문제: ‘당신은 3개의 문 중 하나를 골라 그 문 뒤에 있는 상품을 받는다.", 
            "하나의 문 뒤에는 포르쉐 자동차가 있고 나머지 2개 뒤에는 염소가 있다.",
            "당신이 문을 선택하면 진행자는 나머지 2개 중 염소가 있는 문을 연다.",
            "이제 당신은 처음 고른 문을 계속 선택하거나 아직 닫혀 있는 다른 문으로 바꿀 수 있다.",
            "만약 당신이 자동차를 받으려면 문을 바꿔야할까? / 아니면 바꾸지 않아야 할까?",
            "",
            "해설: 몬티홀 문제에서 처음 고른 문이 차일 확률은 33.3%이다.",
            "그리고 나머지 두 문이 차일 확률은 66.6%이다.",
            "몬티홀은 나머지 두 문중 염소인 문을 열기때문에 문을 바꿀경우와 안바꿀 경우 50%로 오해할 수 있지만 ",
            "0.000001%의 로또를  맞았다고 로또를 맞을 확률이 100%가 되는 것이 아닌것 처럼 50 : 50이 아닌 33.3 : 66.6으로 문을 바꾸는 것이 이득이다.",
            "몬티홀 문제를 쉽게 이해하기 위해 염소문 99개 자동차 문 1개로 생각하는 것도 좋은 생각이다.",
            "당신이 고른 문에서 자동차가 있을 확률은 1%이다. 하지만 나머지 문에 자동차가 있을 확률은 99%이다. 따라서 몬티홀 문제는 문을 바꾸는 것이 당첨 확률이 높다"));
        item4.setItemMeta(meta);
        //0 1. 2 3 4. 5 6 7. 8
        inven.setItem(13, item4);
        inv.setItem(1,item1);
        inv.setItem(4,item2);
        inv.setItem(7,item3);
        p.openInventory(inv);
    }
}
//   ’ 
 

   
 
